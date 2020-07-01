import hashlib
from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, orm
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from libs.database.types import LaboratoryTypes
from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class QueryStrategy:

    def __init__(self, user):
        self.user = user

    def gen_sy_query(self, session):
        from api.models.match import Match

        matched_user_ids = list(set([x.to_user_id for x in session.query(Match).filter((Match.from_user_id == self.user.id))] + \
        [x.from_user_id for x in session.query(Match).filter((Match.to_user_id == self.user.id))]))

        return {
            'query': {
                'function_score': {
                    'query': {
                        'bool': {
                            'must': [
                                {'term': {'sex': not self.user.sex}}
                            ],
                            'must_not': [
                                {'terms': {'_id': matched_user_ids}} # 빈 배열이어도 정상동작 확인 2020-06-29
                                # TODO: 정지 당한 계정도 must_not 해야 함. {'lt': {'frozen_until': 현재시각 YYYY-MM-DD }}
                                # TODO: 자신과 비슷한 티어가 우선순위를 같도록 해야 함.
                            ]
                        }
                    } ,
                    'boost': '5',
                    'functions': [
                        {
                            'filter': { 'terms': {'animal_id': list(x.to_animal_ids)} },
                            'weight': x.weight
                        } for x in self.user.animal.correlations
                    ]
                }
            }
        }


class User(Base):
    __tablename__ = 'users'
    email = Column(TEXT)
    frozen_until = Column(DATETIME)
    frozen_at = Column(DATETIME)

    # 신상정보
    name = Column(CHAR(50))
    age = Column(INTEGER)
    sex = Column(BOOLEAN) # 0 은 남자 1 은 여자
    nick_name = Column(CHAR(50), unique=True)
    education = Column(TEXT) # 학력
    occupation = Column(TEXT) # 직업
    occupation_confirmed = Column(BOOLEAN)
    occupation_confirmed_at = Column(DATETIME)
    company = Column(TEXT) # 직장
    pictures = Column(LaboratoryTypes.TextTuple)
    bio = Column(TEXT) # 인삿말
    phone = Column(CHAR(20), unique=True, nullable=True)
    phone_registered = Column(BOOLEAN)
    location1 = Column(TEXT)
    location2 = Column(TEXT)
    height = Column(INTEGER)
    body_shape = Column(TEXT) # 체형
    religion = Column(TEXT)
    hobby = Column(TEXT)
    speciality = Column(TEXT) # 특기
    interest = Column(TEXT) # 관심사
    drink = Column(TEXT) # 음주
    cigarette = Column(TEXT) # 흡연
    animal_id = Column(Integer, ForeignKey('animals.id', ondelete='CASCADE'))
    animal = relationship('Animal', lazy="selectin", uselist=False, backref=backref('user', uselist=False))

    # el_time
    el_time = Column(TIMESTAMP) # elasticsearch 에 수정사항을 반영해야 한다면 이 컬럼을 갱신 하세요!

    # 이상형 정보
    ideal_age_start = Column(INTEGER)
    ideal_age_end = Column(INTEGER)
    ideal_body_shape = Column(TEXT)
    ideal_type_groups = Column(LaboratoryTypes.IntTuple)
    ideal_height_start = Column(INTEGER)
    ideal_height_end = Column(INTEGER)

    # 회원가입 전 까지 쓸 정보
    registration_phase = Column(CHAR(10)) # 회원가입 중간에 껐다가 다시 할 수 있도록 만들어야 할 듯.
    registration_confirmed = Column(BOOLEAN, server_default='0')
    registration_confirmed_at = Column(DATETIME) # 최종 승인!

    # statistics
    registered_at = Column(DATETIME)  # 회원가입 통계낼 때 유용
    last_access = Column(DATETIME)  # 통계낼 때 유용

    # fcm
    fcm_token = Column(TEXT)

    # oauth
    # oauth_google_id = Column(Integer, ForeignKey('oauth_google.id', ondelete='CASCADE'))
    # oauth_kakao_id = Column(Integer, ForeignKey('oauth_kakao.id', ondelete='CASCADE'))
    # oauth_naver_id = Column(Integer, ForeignKey('oauth_naver.id', ondelete='CASCADE'))
    # oauth_apple_id = Column(Integer, ForeignKey('oauth_apple.id', ondelete='CASCADE'))

    # 다음 backref 가 존재합니다.
    # point
    # oauth_google
    # oauth_kakao
    # oauth_facebook
    # oauth_apple

    # put 으로 변경할 수 없는 컬럼 들입니다.
    sensitives = {'email', 'password', 'phone', 'fcm_token', 'registered_at', 'last_access'}

    @orm.reconstructor
    def init_on_load(self):
        self.strategy = QueryStrategy(self)

    @property
    def oauth(self):
        if self.oauth_google_id:
            return self.oauth_google
        if self.oauth_kakao_id:
            return self.oauth_kakao
        if self.oauth_naver_id:
            return self.oauth_naver
        if self.oauth_apple_id:
            return self.oauth_apple

    def __init__(self, **kwargs):
        '''
        :param kwargs:
        '''
        super().__init__(**kwargs)
        now =  datetime.now()
        self.registered_at = now
        self.last_access = now
        self.el_time = now

    def gen_sy_query(self, session):
        '''
        백엔드 로직에서 쓸 일이 없습니다. 따라서 session 을 특별히 인자로 전달 받습니다.
        '''
        return self.strategy.gen_sy_query(session)

    def json(self, **kwargs):
        result = {
            'id': self.id,
            'email': self.email,

            # 신상 정보
            'name': self.name,
            'nick_name': self.nick_name,
            'education': self.education,
            'occupation': self.occupation,
            'occupation_confirmed': self.occupation_confirmed,
            'occupation_confirmed_at': self.occupation_confirmed_at,
            'company': self.company,
            'pictures': self.pictures,
            'bio': self.bio,
            'phone': self.phone,
            'phone_registered': self.phone_registered,
            'location1': self.location1,
            'location2': self.location2,
            'height': self.height,
            'body_shape': self.body_shape,
            'religion': self.religion,
            'hobby': self.hobby,
            'speciality': self.speciality,
            'interest': self.interest,
            'drink': self.drink,
            'cigarette': self.cigarette,

            # 기타
            'registration_phase': self.registration_phase,

            # 통계 정보
            'last_access': DateTimeHelper.full_datetime(self.last_access),
            'registered_at': DateTimeHelper.full_datetime(self.registered_at),
        }

        if self.phone:
            result['phone'] = self.phone

        if kwargs.get('with_point'):
            result['hp'] = self.point.hp
            result['mp'] = self.point.mp

        return result

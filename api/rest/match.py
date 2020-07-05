from datetime import datetime, timedelta

from api.models.match import Match
from libs.database.engine import Session
from libs.route.router import route
from flask import g
from sqlalchemy import or_

from libs.status import Status


@route
def get_soyeon_matches():
    '''
    '소연이 제안하는 인연' 을 조회합니다.
    '''
    matches = Session().query(Match).filter(or_(Match.from_user_id == g.user_session.user.id
                                      , Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_SOYEON)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_preference_matches():
    matches = Session().query(Match).filter(or_(Match.from_user_id == g.user_session.user.id
                                      , Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_PREFER)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_old_matches():
    matches = Session().query(Match).filter((Match.created_at <= (datetime.now() - timedelta(days=2)).date())).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_random_matches():
    matches = Session().query(Match).filter(or_(Match.from_user_id == g.user_session.user.id
                                      , Match.to_user_id == g.user_session.user.id)
                                  & (Match.type_ == Match.TYPE_RANDOM)
                                  & (Match.matched == False)
                                  & (Match.created_at >= (datetime.now() - timedelta(days=2)).date())
                                  ).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK


@route
def get_matched_matches():
    matches = Session().query(Match).filter(or_(Match.from_user_id == g.user_session.user.id
                                      , Match.to_user_id == g.user_session.user.id)
                                  & (Match.matched == True)).all()
    return {'matches': [x.json() for x in matches]}, Status.HTTP_200_OK



# TODO: 당신에게 관심있는 인연 + 당신에게 높은 점수를 준 인연
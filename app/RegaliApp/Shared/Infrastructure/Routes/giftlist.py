import os
from app import app
from flask_login import current_user
from flask import redirect, url_for, json, request
from injector import inject
import sys

from app.RegaliApp.List.Infrastructure.Repositories.AlchemyGiftListRepository import AlchemyGiftListRepository
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftList, AlchemyGiftListElement
from app.RegaliApp.List.Application.UseCases import GetGiftList
from app.RegaliApp.List.Application.UseCases import GetGiftLists
from app.RegaliApp.List.Application.UseCases import DeleteGiftList
from app.RegaliApp.List.Application.UseCases import CreateGiftList

from app.RegaliApp.Shared.Infrastructure.Routes.authentication import token_required


@inject
@app.route('/giftlists', methods=['POST'])
@token_required
def post_giftlist(current_user, use_case: CreateGiftList.UseCase):
    gift_list_request = CreateGiftList.Request(
        1,
        request.json['name']
    )

    gift_list = use_case.execute(gift_list_request)

    return {
        'reference': gift_list.reference 
    }

@inject
@app.route('/giftlists/<reference>', methods=['GET'])
@token_required
def get_giftlist(current_user, use_case: GetGiftList.UseCase, reference):
    giftlists = use_case.execute(GetGiftList.Request(reference))

    return giftlists


@inject
@app.route('/giftlists', methods=['GET'])
@token_required
def get_giftlists(current_user, use_case: GetGiftLists.UseCase):
    giftlists = use_case.execute()

    return giftlists


@inject
@app.route('/giftlists/<reference>', methods=['DELETE'])
@token_required
def delete_giftlists(current_user, use_case: DeleteGiftList.UseCase, reference):
    use_case.execute(DeleteGiftList.Request(reference))

    return {
        'message': 'List Deleted'
    }

import os
from app import app
from flask_login import current_user
import uuid
from flask import redirect, url_for, json
from injector import inject
import sys

from app.RegaliApp.List.Infrastructure.Repositories.AlchemyGiftListRepository import AlchemyGiftListRepository
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftList, AlchemyGiftListElement
from app.RegaliApp.List.Application.UseCases.GetGiftList.GetGiftList import GetGiftListUseCase


@app.route('/giftlists', methods=['POST'])
def post_giftlist():
    gift_list = AlchemyGiftList(
        None,
        str(uuid.uuid4()),
        1,
        'Lista de prueba',
        True,       
        True,
        None,
        None
    )

    gift_list.elements.append(
        AlchemyGiftListElement(
            None,
            str(uuid.uuid4()),
            None,
            'Otra Prueba',
            'www.wiii.com',
            None,
            None            
        )
    )

    AlchemyGiftListRepository.save(gift_list)

    return 'post_giftlist'

@inject
@app.route('/giftlists/<reference>', methods=['GET'])
def get_giftlists(use_case: GetGiftListUseCase, reference):
    giftlists = use_case.execute(reference)

    return giftlists.name

@app.route('/giftlists/<reference>', methods=['DELETE'])
def delete_giftlists(reference):
    AlchemyGiftListRepository.deleteListByReference(reference)

    return 'ok'

from flask import request
from flask_login import current_user
from injector import inject

from app import app
from app.regali_app.list.application.use_cases import (
    get_gift_list,
    get_gift_lists,
    delete_gift_list,
    create_gift_list,
    delete_gift_list_element,
    create_gift_list_element
)
from app.regali_app.shared.infrastructure.routes.authentication import token_required


@inject
@app.route('/giftlists', methods=['POST'])
@token_required
def post_giftlist(
    use_case: create_gift_list.UseCase,
    request_data_transformer: create_gift_list.RequestDataTransformer
):
    return use_case.execute(
        request_data_transformer.transform(
            current_user.id,
            request
        )
    )


@inject
@app.route('/giftlists/<reference>', methods=['GET'])
@token_required
def get_giftlist(use_case: get_gift_list.UseCase, reference):
    giftlists = use_case.execute(get_gift_list.Request(reference))

    return giftlists


@inject
@app.route('/giftlists', methods=['GET'])
@token_required
def get_giftlists(use_case: get_gift_lists.UseCase):
    giftlists = use_case.execute()

    return giftlists


@inject
@app.route('/giftlists/<reference>', methods=['DELETE'])
@token_required
def delete_giftlists(use_case: delete_gift_list.UseCase, reference):
    use_case.execute(delete_gift_list.Request(reference))

    return {
        'message': 'List Deleted'
    }


@inject
@app.route('/giftlists/<reference>/elements', methods=['POST'])
@token_required
def post_giftlist_element(use_case: create_gift_list_element.UseCase, reference):
    return use_case.execute(
        create_gift_list_element.Request(reference, request.json['url'])
    )



@inject
@app.route('/giftlists/<list_reference>/elements/<element_reference>', methods=['DELETE'])
@token_required
def delete_giftlist_element(
    use_case: delete_gift_list_element.UseCase,
    list_reference,
    element_reference
):
    use_case.execute(
        delete_gift_list_element.Request(
            list_reference,
            element_reference
        )
    )

    return {
        'message': 'List Element Deleted'
    }

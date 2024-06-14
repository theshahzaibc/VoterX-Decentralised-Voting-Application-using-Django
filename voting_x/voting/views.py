from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .contract import voting_contract, web3


def index(request):
    return render(request, 'index.html')


@csrf_exempt  # Apply csrf_exempt decorator to the view
def get_candidates(request):
    candidates = voting_contract.functions.getCandidates().call()
    candidate_list = [{'id': c[0], 'name': c[1], 'voteCount': c[2]} for c in candidates]
    return JsonResponse(candidate_list, safe=False)


@csrf_exempt  # Apply csrf_exempt decorator to the view
def register_voter(request):
    address = request.POST.get('address')
    if not web3.is_address(address):
        return JsonResponse({'status': 'Invalid voter address'})
    tx_hash = voting_contract.functions.registerVoter(address).transact({'from': web3.eth.default_account})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return JsonResponse({'status': 'Voter registered successfully'})


@csrf_exempt  # Apply csrf_exempt decorator to the view
def start_voting(request):
    tx_hash = voting_contract.functions.startVoting().transact({'from': web3.eth.default_account})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return JsonResponse({'status': 'Voting started'})


@csrf_exempt  # Apply csrf_exempt decorator to the view
def end_voting(request):
    tx_hash = voting_contract.functions.endVoting().transact({'from': web3.eth.default_account})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return JsonResponse({'status': 'Voting ended'})


@csrf_exempt  # Apply csrf_exempt decorator to the view
def cast_vote(request):
    address = request.POST.get('address')
    candidate_id = int(request.POST.get('candidate_id'))
    if not web3.is_address(address):
        return JsonResponse({'status': 'Invalid address'})
    if candidate_id == "":
        return JsonResponse({'status': 'Invalid candidate id'})
    tx_hash = voting_contract.functions.vote(candidate_id).transact({'from': address})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return JsonResponse({'status': 'Vote casted successfully'})

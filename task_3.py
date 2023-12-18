def compare_json(json1, json2, diff_list):
    diffs = []
    for key in json1.keys():
        if isinstance(json1[key], dict):
            inner_diffs = compare_json(json1[key], json2[key], diff_list)
            diffs += inner_diffs
        elif key in diff_list and json1[key] != json2[key]:
            diff = {
                'key': key,
                'old_value': json2[key],
                'new_value': json1[key]
            }
            diffs.append(diff)
    return diffs


json = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
        'data': {'id': 11111111, 'company_id': 111111, 'services': [
            {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}],
                 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
                 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
                            'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00',
                 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1,
                 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049,
                 'created_user_id': 10573443, 'deleted': False, 'paid_full': 0,
                 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}

Json_old = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
            'data': {'id': 11111111, 'company_id': 111111, 'services': [
             {'id': 9035445, 'title': 'Стрижка', 'cost': 2000, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}],
                  'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Стилист'},
                  'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
                             'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00',
                  'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1,
                  'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049,
                  'created_user_id': 10573443, 'deleted': False, 'paid_full': 0,
                  'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}

diff_list = ['services', 'staff', 'datetime']

result = compare_json(json, Json_old, diff_list)
print(result)

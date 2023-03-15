from random import randint

colors = ['Yellow', 'Green', 'Red', 'Orange', 'Blue', 'Purple', 'Pink', 'White']
color_number = randint(1, 7)
result_color = colors[color_number]
print("{\"took\" : 1095, \"timed_out\" : false, \"_shards\" : {\"total\" : 0, \"successful\" : 0,\"skipped\" : 0,\"failed\" : 0},\"hits\" : {\"total\" : {\"value\" : 1,\"relation\" : \"eq\"},\"max_score\" : 1.0,\"hits\" : [{\"_index\" : \"\",\"_type\" : \"stats values\",\"_id\" : \"1\",\"_score\" : 1.0,\"_source\" : {\"color\" : \"" + result_color + "\", \"user\" : \"Olivere\",\"message\" : \"Hello, user!\"}}]},\"service_data\" : {\"query_id\" : \"\"}}")

from api_tools.fetcher import fetch_todo

# todo id 1 fetch 
print('fetching data from api ...')
todo_data = fetch_todo(1)

#result print 
print('api responce:', todo_data)
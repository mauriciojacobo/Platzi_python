users ={
    'mauricio':"active",
    'david': 'inactive'
}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
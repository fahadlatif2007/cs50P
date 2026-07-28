import emoji

x = input('input: ')
print(emoji.emojize('output: :thumbs_up:'))
print('output:', emoji.emojize(x, language='alias'))

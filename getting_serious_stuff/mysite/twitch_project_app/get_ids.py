from twitch import TwitchClient

#featured = Streams.get_featured(5, 0)

#print(featured)



#client = TwitchClient(clxient_id='uo6dggojyb8d6soh92zknwmi5ej1q2')


#channel = client.channels.get_by_id(44322889)



#print(channel.id)
#print(channel.name)
#print(channel.display_name)


client = TwitchClient('uo6dggojyb8d6soh92zknwmi5ej1q2')
channels = client.streams.get_featured(limit=25, offset=0)

print(channels)





import numpy as np 
import pandas as pd 

class Graph:
	name = ""
	relations = {}
	def __init__(self, name):
		self.name = name
		self.relations = {}

	def addRelation(song):
		print(relations)
		if (song in relations):
			relations[song] += 1
		else:
			relations[song] = 1
	
	def getRelation():
		return relations


class recommend:

	artists = {}


	def __init__(self):
		self.artists = {}

	def buildGraph(self):
		data = pd.read_csv("matrix.csv")

		#reading the data from the lastfm data set from https://github.com/algorithmica-repository/datascience
		data = pd.read_csv("lastfm.csv")

		#do not need the sex and country for the purposes in my project
		del data['sex']
		del data['country']
		uniqueArtists = data['artist'].unique()
		uniqueUsers = data['user'].unique()

		'''
		Looping through the users artists and seeing if they had it in the unique artist. Assigning 1 for yes
		and 0 for no. 
		'''
		rows = []
		for i in uniqueUsers:
		    user= []
		    normal = data[data.user == i]['artist'].to_dict() #made a dict of each the user to artist from dataframe
		    res = dict((v,k) for k,v in normal.iteritems()) #reversed keys and values
		    for j in uniqueArtists:
		            if j in res:
		                user.append(1)
		            else:
		                user.append(0)
		    rows.append(user)


		# transposed the matrix because I wanted the Artist at the top and the rows in that column to be
		# if the user had the artist in their playlist
		trans = np.array(rows).T


		'''
		Making a dict where artist is the key and the value is a list of the 1s and 0s depending
		on if the users, first to last, had it in their favorite artists.
		'''
		d = {}
		for i in xrange(len(trans)):
		    values = []
		    for j in xrange(len(trans[0])):
		        values.append(trans[i][j])
		    d[uniqueArtists[i]] = values
		
		#for unique artists
		#dictionary of artist and graph nodes
		for artist in uniqueArtists:
			g = Graph(artist)
			artists[artist] = g


		for user in uniqueUsers:
			for artist1 in uniqueArtists:
				for artist2 in uniqueArtists:
					# print(len(uniqueArtists[user]))
					if (artist1 != artist2):
						if (artist1 in artists[artist1].relations):
							artists[artist1].relations[artist1] += 1
						else:
							artists[artist1].relations[artist1] = 1

					print(artists[artist1].relations.keys())

		def getRecommendation(artist):
			if (artist not in uniqueArtists):
				return False
			else:
				new_artist = None
				my_max = 0
				for (key in artists[artist].relations.keys()):
					if (artists[artist].relations[key] > my_max):
						my_max = artists[artist].relations[key]
						new_artist = key

			return key





r = recommend()
r.buildGraph()
r.getRecommendation("tom waits")

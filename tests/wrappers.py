__author__ = "Benoit CAYLA"
__email__ = "admin@datacorner.fr"
__license__ = "MIT"

from src.ragfmk.ragWrapper import ragWrapper
from src.ragfmk.framework.sets.chunks import chunks
from src.ragfmk.framework.documents.documentBaseObject import documentBaseObject
from src.ragfmk.framework.sets.nearest import nearest

"""
	Here is the list of all the blueprism functions that are called from the VBO.
	Note: Modifying one of this function means modifying the code inside the VBO also.
"""

def prompt(prompt, parameters):
	myRag = ragWrapper()
	response, outs = myRag.prompt(prompt, parameters)
	return response, outs, myRag.trace.getFullJSON()

def readdoc(filename, config):
	myRag = ragWrapper()
	response = myRag.read(filename, config)
	return response.content, myRag.trace.getFullJSON()

def chunking(text, config):
	myRag = ragWrapper()
	doc = documentBaseObject()
	doc.content= text
	cks = myRag.chunk(doc, config)
	return cks.size, cks.jsonContent, myRag.trace.getFullJSON()

def textEmbeddings(text, jsonConfig):
	myRag = ragWrapper()
	cks = chunks()
	cks.add(text)
	embeddings = myRag.createEmbeddings(cks, jsonConfig)
	return embeddings.size, embeddings.jsonContent, myRag.trace.getFullJSON()

def chunksEmbeddings(content, jsonConfig):
	myRag = ragWrapper()
	cks = chunks()
	cks.jsonContent = content
	embeddings = myRag.createEmbeddings(cks, jsonConfig)
	return embeddings.size, embeddings.jsonContent, myRag.trace.getFullJSON()

def VS_Store(content, vs_config):
	myRag = ragWrapper()
	myRag.storeEmbeddings(content, vs_config)
	return myRag.trace.getFullJSON()

def VS_Search(content, k, vs_config):
	myRag = ragWrapper()
	try:
		similars = myRag.similaritySearch(k, content, vs_config)
		return similars.jsonContent, myRag.trace.getFullJSON()
	except:
		return "", myRag.trace.getFullJSON()

def faissMemorySearch(k, vp, vc, vs_config):
	myRag = ragWrapper()
	try:
		similars = myRag.memSimilaritySearch(k, vp, vc, vs_config)
		return similars.jsonContent, myRag.trace.getFullJSON()
	except:
		return "", myRag.trace.getFullJSON()

def calcSimilarity(text1, text2, vsCfg, embdsCfg):
	myRag = ragWrapper()
	score = myRag.similarityScore(text1, text2, vsCfg, embdsCfg)
	return score, myRag.trace.getFullJSON()

def buildPrompt(question, content):
	myRag = ragWrapper()
	nr = nearest()
	nr.jsonContent = content
	resp = myRag.buildPrompt(question, nr)
	return resp, myRag.trace.getFullJSON()
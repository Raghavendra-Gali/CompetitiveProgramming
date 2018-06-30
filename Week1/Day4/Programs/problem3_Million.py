import unittest

class TernaryNode():
		def __init__(self):
			self.char=None
			self.left=None
			self.right=None
			self.mid=None
			self.contains=False

class TST(object):

	def __init__(self):
		# super(TST, self).__init__()
		self.root=None

	def add_word(self,word):
	    if word=='':
	        word='\\0'
	   # print(word)
	    if self.get(word)==False:
	        self.root=self.put(self.root,word,0)
	        return True
	    return False

	def put(self,x,word,d):
		c=word[d]
		if x==None:
			x=TernaryNode()
			x.char=c
		if c<x.char:
			x.left=self.put(x.left,word,d)
		if c>x.char:
			x.right=self.put(x.right,word,d)
		elif d<len(word)-1:
			x.mid=self.put(x.mid,word,d+1)
		else:
			x.contains=True
		return x

	def get(self,word):
		x=self.search(self.root,word,0)
# 		print("search",word)
# 		print(x,word)
		if not x:
			return False
		# print(x.contains)
		return x.contains
		
	def search(self,x,word,d):
		if x==None:
			return None
		c=word[d]
		if c<x.char:
			return self.search(x.left,word,d)
		if c>x.char:
			return self.search(x.right,word,d)
		elif d<len(word)-1:
			return self.search(x.mid,word,d+1)
		else:
			return x


class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = TST()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
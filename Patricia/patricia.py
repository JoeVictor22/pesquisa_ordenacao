class patricia():
    def __init__(self):
        self._data = {}
    
    '''
	__repr__ = {nodeIndex : ['word', {nodes}]}
	{node : ['', {}]} 

    '''

    def add(self, word):
        data = self._data
        i = 0
        while 1:
            try:
				#verifica se nesse nivel existe key com a mesma indexação da palavra
                node = data[word[i:i+1]]
            except KeyError:	
                if data:
					#cria a key como indexação do node se ja existir key com o mesmo prefixo
                    data[word[i:i+1]] = [word[i+1:],{}]
                else:
					#se nao existir node
                    if word[i:i+1] == '':
						#se a palavra ja existir
                        return
                    else:
                        if i != 0:
                        	#caso não esteja indexado no primeiro char é preciso criar uma key vazia informando q eh uma palavra
                            data[''] = ['',{}]
                        data[word[i:i+1]] = [word[i+1:],{}]
                return

			#existindo uma key no dicionario q corresponda com o index da palavra
            i += 1
            if word.startswith(node[0],i):
				#se o resto da palavra apos o index é identico ao valor dentro do node
				#registra um node informando q é uma palavra ou parte para o proximo no interno
                if len(word[i:]) == len(node[0]):
                	#verifica se ja verificou tds os char da palavra e retorna
                    if node[1]:
						#cria um item informando q é uma palavra caso nao exista
                        try:
                            node[1]['']
                        except KeyError:
                            data = node[1]
                            data[''] = ['',{}]
                    return
				#acessa o proximo node
                else:
                    i += len(node[0])
                    data = node[1]

			#caso em que é inserido um novo no com prefix ja existente
            else:
                ii = i
                j = 0
                while ii != len(word) and j != len(node[0]) and \
                      word[ii:ii+1] == node[0][j:j+1]:
                    ii += 1
                    j += 1
                tmpdata = {}
                tmpdata[node[0][j:j+1]] = [node[0][j+1:],node[1]]
                tmpdata[word[ii:ii+1]] = [word[ii+1:],{}]
                data[word[i-1:i]] = [node[0][:j],tmpdata]
                return
   
    def addText(self, text):
    	#text = text.strip([',', '.'])
    	text = text.replace(',', '')
    	text = text.replace('.', '')
    	text = text.split(' ')

    	for word in text:
    		self.add(word)


    def isWord(self,word):
        data = self._data
        i = 0
		# acessa node por node em busca da palavra
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return False
            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                        except KeyError:
                            return False
                    return True
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                return False

    def isPrefix(self,word):
        data = self._data
        i = 0
        wordlen = len(word)
		#verifica o inicio da palavra com a key e o valor de cada node
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return False
            i += 1
            if word.startswith(node[0][:wordlen-i],i):
                if wordlen - i > len(node[0]):
                    i += len(node[0])
                    data = node[1]
                else:
                    return True
            else:
                return False

    def remove(self,word):
        data = self._data
        i = 0
        while 1:
        	#checa se o node existe
            try:
                node = data[word[i:i+1]]
            except KeyError:
                print( "Não está presente")
                return
            i += 1
            #busca o node e o remove
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                            node[1].pop('')
                        except KeyError:
                            print( "Não está presente")
                        return
                    data.pop(word[i-1:i])
                    return
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                print ("Não está presente")
                return


	


def main():

	x = patricia()
	x.add('baiacu')
	print(x._data)

	x.add('bacalhau')
	print(x._data)

	x.add('bagre')
	print(x._data)

	print(x.isPrefix('bac'))


if __name__ == "__main__":
	main()

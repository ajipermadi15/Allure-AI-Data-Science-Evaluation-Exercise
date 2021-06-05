import pickle

prd = input('Input your favorite product ID: ')

model, corr_mat = pickle.load(open('D:\AllureAI\model.pkl','rb'))
product_names = list(model.index)
product_ID = product_names.index(prd)
correlation_product_ID = corr_mat[product_ID]
Recommend = list(model.index[correlation_product_ID > 0.70])
Recommend.remove(prd) 

print('We recommend the following products: ')
for i in range(len(Recommend[0:5])):
    print('{}. {}'.format(i+1, Recommend[i]))

print('We hope you enjoy with our recommendations.')
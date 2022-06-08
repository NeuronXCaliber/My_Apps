import numpy as np
import pickle

load_model=pickle.load(open('C:/webappmachinelearning/train_model.sav','rb'))

input=(5,166,72,19,175,22.9,0.56,51)
input_as_numpy=np.asarray(input)
input_reshape=input_as_numpy.reshape(1,-1)
prediction=load_model.predict(input_reshape)
print(prediction)
if (prediction[0] == 0):
  print(" Patient has no diabetes")
else:
  print(" Patient has diabetes")
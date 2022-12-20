import pickle
import json
import config1
import numpy as np

class CellPhonePrice:
    def __init__(self,user_data):
        self.model_file_path = "cellphone_model.pkl"
        self.user_data = user_data
       

    def load_saved_data(self):
        with open(self.model_file_path,'rb') as f:
            self.model = pickle.load(f)
    
    def get_predicted_price(self):
        
        self.load_saved_data()
        Sale = eval(self.user_data["Sale"])
        weight = eval(self.user_data["weight"])
        resoloution = eval(self.user_data["resoloution"])
        ppi = eval(self.user_data["ppi"])
        cpu_core = eval(self.user_data["cpu_core"])
        cpu_freq = eval(self.user_data["cpu_freq"])
        internal_mem = eval(self.user_data["internal_mem"])
        ram = eval(self.user_data["ram"])
        RearCam = eval(self.user_data["RearCam"])
        Front_Cam = eval(self.user_data["Front_Cam"])
        battery = eval(self.user_data["battery"])
        thickness = eval(self.user_data["thickness"])
        

        test_array= np.array([Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness])
       
      
        print(test_array)

        predicted_price = np.around(self.model.predict([test_array])[0],3)
        print('predicted_price:',predicted_price)
        return predicted_price

if __name__ == '__main__':
    bost = CellPhonePrice()
    bost

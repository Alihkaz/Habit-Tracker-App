#
import requests
from datetime import datetime



TOKEN="Your Token From pixe.la "
USERNAME="Your User Name in pixe.la "


pixela_endpoint="https://pixe.la/v1/users"
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"


user_params = {
  "token":TOKEN,
  "username":USERNAME,
  "agreeTermsOfService":"yes",
  "NotMinor":"yes",
  
}

# response=requests.post(url=pixela_endpoint  ,  json=user_params)
# print(response.text)

# once you click run in the first time , it will give an error in the next time since in thye first time the account will be created . 

graph_config = {

  "id":"graph1",
  "name":"Smoking Urge Graph",
  "unit":"commit",
  "type":"int",
  "Color":"sora",
  
 }

headers={
  "X-USER-TOKEN": TOKEN
}


# here we provide the header because the api wants the call in a molre secure way , not in a classical way , were by that wwe will the key more secure

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)

# print(response.text)

# so here we used the method post to give the ap[i a certain data to work with , and here we are specialized with graph design , how ever our account have been created and the graph with our special design have been saved into it successfully , and there is a link with our user name and the id of our graph to visit it ! And it will be done through this link :https://pixe.la/v1/users/v1/users/alikaz/graphs/graph1.html
# and by that we authenticate our selfs bby a more secured and advanced way through the header. 

today=datetime.now()

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config = {

  "date":today.strftime("%Y%m%d"),#here we modify the day we get from the todatmethod in a way that fits the api parameter requirments ! through the function strftime and specifiying some codes ythat we get from the table . 
  "quantity":"1",

  
 }

# here we are sending specific data or locations to edit our table and graph depending on our commitment , and the quantits stands for how much we commit 

# response=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)

# print(response.text)


pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config = {

  "date": "20230523",
  "quantity":"3",

  
 }
response=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)


# editing the data we provided :

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230522"
new_pixel_config = {

 
  "quantity":"4",

  
 }
response=requests.put(url=pixel_endpoint,json=new_pixel_config,headers=headers)
print(response.text)

#delete the data we provided 

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230522"

response=requests.delete(url=pixel_endpoint,headers=headers)
print(response.text)
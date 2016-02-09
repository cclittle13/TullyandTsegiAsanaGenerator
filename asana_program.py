import json
with open("yoga_asanas_json.json") as json_data:
    data = json.load(json_data)
    #to add more data from different APIs, you can change this information 

total_time = 0

total_practice = []
# total_practice.items()
# total_practice.keys()
# ratings.values()

    #
#elif integration_question1 == "No":
    #print "NO: zero_minutes"

    #integration_question1 = input()
    #total_practice = int(integration_question1)



#total_practice.items()
#total_practice.keys()
#total_practice.values()

# print total_practice


# for key in total_practice: 
#     print key 


integrations = data.keys()

for key in integrations:
    print "Do you want to add the %s Series? " %key
    answer = raw_input('>')
    if answer == "Yes":
        print data[key]['Time'], 'minutes'
        total_practice.append(key)
        total_time += data[key]['Time']
        if total_time >= 60:
            print "You've exceeded the 60 minute time limit."
            break



# integration_question1 = raw_input ("Do you want to add the Integration Series? ")
# print integration_question1
# if integration_question1 == "Yes":
#     print data['Integration']['Time'], 'minutes'
#     total_practice.append("Integration")
#     total_time += data['Integration']['Time']


# integration_question2 = raw_input ("Do you want to add the Intention Series? ")
# print integration_question2
# if integration_question2 == "Yes":
#     print data['Intention']['Time'], 'minutes'# YES: 4_minutes' #ADD CORRECT TIME FOR 2-13 !!!!!!!!!!!!
#     total_practice.append("Intention")
#     total_time += data['Intention']['Time']

 
# integration_question3 = raw_input ("Do you want to add the Sun Salutation A Series? ")
# print integration_question3
# if integration_question3 == "Yes":
#     print data['Sun_Salutation_A']['Time'], 'minutes'
#     total_practice.append("Sun_Salutation_A")
#     total_time += data['Sun_Salutation_A']['Time']                                                                              
 
# integration_question4 = raw_input ("Do you want to add the Sun Salutation B Series? ")
# print integration_question4
# if integration_question4 == "Yes":
#     print data['Sun_Salutation_B']['Time'], 'minutes'
#     total_practice.append("Sun_Salutation_B") 
#     total_time += data['Sun_Salutation_B']['Time']                                                                                     

 
# integration_question5 = raw_input ("Do you want to add the Core Strengthening Series? ")
# print integration_question5
# if integration_question5 == "Yes":
#     print data['Core_Strengthening_Series']['Time'], 'minutes'
#     total_practice.append("Core_Strengthening_Series") 
#     total_time += data['Core_Strengthening_Series']['Time']                                                                                    
                                                                                         

 
# integration_question6 = raw_input ("Do you want to add the Crescent Lunge Series? ")
# print integration_question6
# if integration_question6 == "Yes":
#     print data['Crescent_Lunge_Series']['Time'], 'minutes'
#     total_practice.append("Crescent_Lunge_Series")      
#     total_time += data['Crescent_Lunge_Series']['Time']                                                                  

 
# integration_question7 = raw_input ("Do you want to add the Balancing Series? ")
# print integration_question7
# if integration_question7 == "Yes":
#     print data['Balancing_Series']['Time'], 'minutes'
#     total_practice.append("Balancing_Series")          
#     total_time += data['Balancing_Series']['Time']                                                                 
                                                                          

 
# integration_question8 = raw_input ("Do you want to add the Triangle Series? ")
# print integration_question8
# if integration_question8 == "Yes":
#     print data['Triangle_Series']['Time'], 'minutes'
#     total_practice.append("Triangle_Series")         
#     total_time += data['Triangle_Series']['Time']                                                  

 
# integration_question9 = raw_input ("Do you want to add the Hip Opener Series? ")
# print integration_question9
# if integration_question9 == "Yes":
#     print data['Hip_Opener_Series']['Time'], 'minutes'
#     total_practice.append("Hip_Opener_Series")    
#     total_time += data['Hip_Opener_Series']['Time']                                                         

 
# integration_question10 = raw_input ("Do you want to add the Spine Strengthening Series? ")
# print integration_question10
# if integration_question10 == "Yes":
#     print data['Spine_Strengthening_Series']['Time'], 'minutes'
#     total_practice.append("Spine_Strengthening_Series")       
#     total_time += data['Spine_Strengthening_Series']['Time']                                                   

 
# integration_question11 = raw_input ("Do you want to add the Forward Fold Series? ")
# print integration_question11
# if integration_question11 == "Yes":
#     print data['Forward_Fold_Series']['Time'], 'minutes'
#     total_practice.append("Forward_Fold_Series")   
#     total_time += data['Forward_Fold_Series']['Time']


# integration_question12 = raw_input ("Do you want to add the Surrender Series? ")
# print integration_question12
# if integration_question12 == "Yes":
#     print data['Surrender_Series']['Time'], 'minutes'
#     total_practice.append("Surrender_Series")        
#     total_time += data['Surrender_Series']['Time']


# integration_question13 = raw_input ("Do you want to add Namaste? ")
# print integration_question13
# if integration_question13 == "Yes":
#     print data['Namaste']['Time'], 'minutes'
#     total_practice.append("Namaste")  
#     total_time += data['Namaste']['Time']



# for key in total_practice: 
#     print key 

for item in total_practice:
    key_for_asanas = data[item]
    time_for_asana = key_for_asanas['Time']
    print time_for_asana  # gives you your total time


for key in total_practice:
    for item in data[key]:
        print item , '\t\t', data[key][item]
    print '*'*80
  

print 'Total =', total_time


# we GOT time back
# while loop :  while time >= 60 && < 90:
    # increment time
    # do what you want
# parse through the sequence and print a pretty way
# print their asana  "this is your sequence"

#print"".format()
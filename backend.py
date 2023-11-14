import pandas as pd

data=pd.read_csv('C:\Users\User\Desktop\SE_PROJECT\SE_dataset.csv')
print(data.columns)
print("Select your field: Engineering, Medical\n")
stream=input()


if stream=='Medical':
    df=data[data['Field ']=='Medical'].sort_values(by='NEET cut off',ascending=True)
    print(df)
    print("Provide Your NEET score: \n")
    score=int(input())
    if score<381 :
        print('No college available :(')

    elif score>381 and score<721:
        df=df[df['NEET cut off']<=score]
        print(df)
        print('select a location')
        print(df['Location'].unique())
        loc=input()
        if loc in df['Location'].unique():
            df=df[df['Location']==loc]
            if len(df)==0:
                print('no colleges available')
            else:
                print('select a college')
                print(df['University name '])
    
    else:
        print("Wrong input")

elif stream=='Engineering':
    print("Select your Course: CS, MECH, CIVIL, ECE\n")
    branch=input()
    if branch in data['Course'].unique():
        df=data[data['Course']==branch].sort_values(by='JEE cut off',ascending=True)
        print(df)
        print('Share your JEE score')
        score=float(input())
        if score <100:
            df=df[df['JEE cut off']<=score]
            if len(df)==0:
                print('no colleges available')
            else:
                print(df['University name '])
        else:
            print('wrong input')


else:
    print('wrong input')
    

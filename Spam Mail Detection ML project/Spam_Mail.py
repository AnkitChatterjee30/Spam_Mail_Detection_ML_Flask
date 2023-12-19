import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
def spam_prediction(message :list):
    df=pd.read_csv("mail_data.csv")
    df.loc[df['Category']=='spam','Category',]=0
    df.loc[df['Category']=='ham','Category',]=1
    X = df['Message']
    Y=df['Category']
    X_train, X_test, Y_train, Y_test= train_test_split(X,Y, random_state=3, test_size=0.2)
    feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    X_train_features = feature_extraction.fit_transform(X_train)
    X_test_features = feature_extraction.transform(X_test)
    Y_train = Y_train.astype('int')
    Y_test = Y_test.astype('int')
    model = LogisticRegression()
    model.fit(X_train_features, Y_train)
    mess=feature_extraction.transform(message)
    return (model.predict(mess))[0]
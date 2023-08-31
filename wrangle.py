def wrangle_zillow():
    def get_connection(db, user=env.user, host=env.host, password=env.password):
        return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    def get_zillow_data():
        filename = "sfr_2017.csv"

        if os.path.isfile(filename):

            return pd.read_csv(filename, index_col=0)
        else:
            # Create the url
            url = get_connection('zillow')

            # Read the SQL query into a dataframe
            df = pd.read_sql('''SELECT 
                bathroomcnt, 
                bedroomcnt, 
                calculatedfinishedsquarefeet,
                taxvaluedollarcnt,
                yearbuilt,
                taxamount,
                fips
            FROM properties_2017
            JOIN propertylandusetype
                ON propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid
            WHERE propertylandusetype.propertylandusetypeid = '261';'''
            , url)


            # Write that dataframe to disk for later. Called "caching" the data for later.
            df.to_csv(filename)

            # Return the dataframe to the calling code
            return df
    df = get_zillow_data()
    df.replace(0, np.nan, inplace=True)
    df = df.dropna() 
    return df   
def predict_energy_usage(data_file_path, month_name, temperaturec):
        def linear_regression(X, y):
            X = np.hstack((np.ones((X.shape[0], 1)), X))
            theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
            return theta
        data = pd.read_csv(data_file_path)
        if month_name.capitalize() not in data['Month'].unique() or temperaturec < -10 or temperaturec > 50:
            return None

        month_data = data[data['Month'] == month_name.capitalize()]

        energy_adj = 1
        if temperaturec > 20:
            energy_adj = 1.1
        elif temperaturec < 7:
            energy_adj = 1.2
        else:
            energy_adj = 0.8

        season_adj = 1
        if month_name.capitalize() in ["November", "December", "January", "February"]:
            season_adj = 1.2
        elif month_name.capitalize() in ["September", "October"]:
            season_adj = 1.1

        X = month_data['Temperature(C)'].values.reshape(-1, 1)
        y = month_data['Energy'].values.reshape(-1, 1)
        y = y * energy_adj * season_adj

        theta = linear_regression(X, y)

        temperaturef = temperaturec * 9/5 + 32
        prediction = theta[0][0] + theta[1][0] * temperaturef * energy_adj * season_adj

        draw_graph(data, prediction, month_name.capitalize())
        
        return prediction

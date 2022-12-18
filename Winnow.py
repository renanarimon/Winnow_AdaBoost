import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('winnow_vectors.txt', sep='\s+', header=None)
    X = df.iloc[:, :-1].values
    n_samples, n_features = X.shape
    Y = df.iloc[:, -1].replace(0, -1).values

    W = np.ones((n_features, ))
    Y_pred = np.ones((n_samples, ))
    print(W.shape)
    errors = 0
    tmp_err = 1

    while tmp_err > 0:
        tmp_err = 0
        for i in range(n_samples):
            d = np.dot(W, X[i])
            if d >= n_features:
                Y_pred[i] = 1
            else:
                Y_pred[i] = -1

            if Y_pred[i] != Y[i]:
                errors += 1
                tmp_err += 1
                if Y_pred[i] == 1:
                    for j in range(n_features):
                        if X[i][j] == 1:
                            W[j] = 0

                else:
                    for j in range(n_features):
                        if X[i][j] == 1:
                            W[j] *= 2
                break
    print(errors)


    def test():
        Y_pred_test = np.ones(200, )
        for k in range(200):
            d = np.dot(W, X[k])
            if d >= n_features:
                Y_pred_test[k] = 1
            else:
                Y_pred_test[k] = -1

        print(Y == Y_pred_test)

    # test()





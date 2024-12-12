import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model, datasets
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


#线性回归
def linear_regression():
    # 示例数据集
    # X为特征，y为目标变量
    X = np.array([[1, 1], [1, 2], [2, 3], [2, 4], [3, 5], [4, 6]])
    y = np.array([1, 2, 3, 4, 5, 6])

    # 划分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 创建并训练线性回归模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 进行预测
    y_pred = model.predict(X_test)

    # 评估模型
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # 输出模型的参数
    print("Model intercept:", model.intercept_)
    print("Model coefficients:", model.coef_)


def Linear_Regression_training():
    # Load the diabetes dataset
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]  #np.newaxis增加一维 // 需二维数组

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()  #普通最小二乘线性回归

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)
    #self = fit(self,x,y,sample_weight = None) 拟合线性模型
    #x -> 训练数据
    #y -> 目标标签
    #sample_weight -> 每个样本的权重
    #self -> 返回估计器的实例

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)
    #self = predict(self,x) 使用线性模型进行预测
    #x -> 样本数据
    #self -> 预测值

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print('Mean squared error: %.2f'
          % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    #loss = sklearn.metrics.mean_squared_error(y_true, y_pred, *, sample_weight=None, multioutput='uniform_average', squared=True) 均方误差回归损失
    #y_true -> 真实目标值
    #y_pred -> 预测目标值
    #sample_weight -> 样本权重
    #multioutput -> 定义多个输出值的汇总
    #squared -> 若为True,则返回MSE值,若为False,返回RMSE值
    #loss -> 非负浮点值(最佳值为0.0)或浮点值数组,每个目标对应一个浮点值

    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))
    #z = sklearn.metrics.r2_score(y_true, y_pred, *, sample_weight=None, multioutput='uniform_average')#R^2（确定系数）回归得分函数/最佳可能得分为1.0,并且可能为负
    #y_true -> 真实目标值
    #y_pred -> 预测目标值
    #sample_weight -> 样本权重
    #multioutput -> 定义多个输出分数的汇总,默认值为'uniform_average'
                                            #- ‘raw_values’:
                                            #如果是多输出格式的输入，则返回完整的分数集
                                            #- ‘uniform_average’:
                                            #所有产出的分数均以统一权重平均
                                            #- ‘variance_weighted’:
                                            #将所有输出的分数平均, 并按每个单独输出的方差加
    #z -> 如果‘multioutput’为‘raw_values’，则为R^2分数或分数的ndarray

    # Plot outputs
    plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
    plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()


if __name__ == '__main__':
    Linear_Regression_training()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


if __name__ == '__main__':
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
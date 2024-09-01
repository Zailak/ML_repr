import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    dim = data.shape[1]
    r = np.random.random(dim)
    i = 0
    while i < num_steps:
        r = data @ r / np.linalg.norm(data @ r)
        mu = (r.T @ data @ r) / (r.T @ r)
        i = i + 1
    return mu.item(), r
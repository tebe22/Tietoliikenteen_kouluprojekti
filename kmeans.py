import numpy as np

def laske_etaisyys(piste1, piste2):
    return np.linalg.norm(piste1 - piste2)

def kmeans(data, keskipisteet, max_iter=100):
    numberOfRows = data.shape[0]
    centerPointCumulativeSum = np.zeros_like(keskipisteet)
    counts = np.zeros((6,))
    for _ in range(max_iter):
        for i in range(numberOfRows):
            etaisyydet = [laske_etaisyys(data[i], kp) for kp in keskipisteet]
            voittaja_index = np.argmin(etaisyydet)
            centerPointCumulativeSum[voittaja_index] += data[i]
            counts[voittaja_index] += 1

        for j in range(6):
            if counts[j] != 0:
                keskipisteet[j] = centerPointCumulativeSum[j] / counts[j]
            else:
                keskipisteet[j] = np.random.rand(3) * np.max(data)

        centerPointCumulativeSum.fill(0)
        counts.fill(0)

    return keskipisteet

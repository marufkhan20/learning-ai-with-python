# Starting values
prediction = 3.0
target = 5.0
learning_rate = 0.1

print(f"Starting Prediction: {prediction}")

# Run 10 steps of Gradient Descent 🧗
for epoch in range(1, 11):
    # 1. Measure error and loss 📉
    error = prediction - target
    print(f"error: {error}")
    loss = error ** 2
    print(f"loss: {loss}")
    
    # 2. Calculate gradient (derivative of squared error) 📐
    gradient = 2 * error
    print(f"gradient: {gradient}")
    
    # 3. Update prediction 🔄
    prediction = prediction - (learning_rate * gradient)
    print(f"prediction: {prediction}")
    
    print(f"Step {epoch}: Prediction = {prediction:.3f} | Loss = {loss:.4f}")
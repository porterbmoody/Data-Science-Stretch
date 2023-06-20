---
title: "Linear Algebra and Multivariable Calculus is All you Need"
---


## Background

A Neural Network is a type of artifitial intelligence model that uses linear algebra and multivariable calculus to learn and store the relationship between an input vector and an output vector that minimizes the loss function. Here is lined out the mathematics for a single layer neural network.

Note: DNN's (Deep Neural Networks) or neural networks with more than 1 hidden layer will be covered in another article.

## Prerequisites:
- Transformations, mappings, vector and matrix multiplication and other operations from linear algebra
- Partial derivatives and their implications from multivariable calculus

## Forward Propagation
The input, hidden, and output layers are represented by the following vectors, respectively.


$$
\vec{x} =
\begin{bmatrix}
	x_1\\
	x_2\\
	\vdots\\
	x_m
\end{bmatrix} \in \mathbb{R^m}
,
\vec{h} =
\begin{bmatrix}
	h_1\\
	h_2\\
	\vdots\\
	h_h
\end{bmatrix} \in \mathbb{R^h}
,
\vec{y} =
\begin{bmatrix}
	y_1\\
	y_2\\
	\vdots\\
	y_n
\end{bmatrix} \in \mathbb{R^n}
$$


Let $T_1: \mathbb{R^m}	\rightarrow \mathbb{R^h}$ be a linear mapping. $T_1$ maps the input layer vector $\vec{x} \in \mathbb{R^m}$ to the hidden layer vector  $\vec{h} \in \mathbb{R^h}$. We will use the sigmoid ($\sigma$) activation function which has a domain of $(-\infty,\infty)$ and range of $(-1,1)$. Therefore the the codomain of $T_1$ is $(-1,1)$.


$$
\begin{gather}
W_1 =
	\begin{bmatrix}
	w_{1,1} & w_{1,2} & \ldots & w_{1,m}\\
	w_{2,1} & w_{2,2} & \ldots & w_{2,m}\\
	\vdots & \vdots & \ddots & \vdots\\
	w_{h,1} & w_{h,2} & \ldots & w_{h,m}\\
	\end{bmatrix}
\newline
T_1(\vec{x}) = \sigma(W_1\vec{x}) = \vec{s}

\end{gather}
$$


And let $T_2: \mathbb{R^h}	\rightarrow \mathbb{R^n}$ be a linear mapping. $T_2$ maps the hidden layer vector $\vec{h} \in \mathbb{R^h}$ to the output layer vector  $\vec{y} \in \mathbb{R^n}$.


$$
\begin{gather}
W_2 = \begin{bmatrix}
	w_{1,1} & w_{1,2} & \ldots & w_{1,h}\\
	w_{2,1} & w_{2,2} & \ldots & w_{2,h}\\
	\vdots & \vdots & \ddots & \vdots\\
	w_{n,1} & w_{n,2} & \ldots & w_{n,h}\\
	\end{bmatrix}

\newline
T_2(\vec{h}) = W_2\vec{h} = \vec{y}

\end{gather}
$$


These weight matrices are initally composed of randomly generated scalars, but during backpropagation the values of the true weights are esitmated. The hypothesis of the neural network is that the true weight matrices for the given transformation explains the true relationship between the input and output vectors.

To summarise the forward propogations process...

$$
T_1(\vec{x}) = \sigma(W_1\vec{x}) = \vec{s}
\newline
T_2(\vec{h}) = W_2\vec{h} = \vec{y}

$$

## Back Propgation

If you haven't already been mezmerised, get ready for the real magic show: back progagation. It is the process of adjusting the weights and biases in direction of the local minimun of the loss function with respect to each individual weight as computed by the partial derivative of the loss function with respect to the given weight.





---
title: pizza
---


## Background

A Neural Network is typically a type of machine learning model that use linear algebra and multivariable calculus to create a mapping from an input vector to an output vector that minmizes the loss function. Here is lined out the mathematics for a single layer neural network.

Note: DNN's (Deep Neural Networks) or neural networks with more than 1 hidden layer will be covered in another article.

## Prerequisites:
- Transformations, mappings, vector and matrix multiplication and other operations from linear algebra
- Partial derivatives from multivariable calculus

## Feed Forward Process

The transformation $T_1: \mathbb{R^n}	\rightarrow \mathbb{R^h}$ maps the input vector $\vec{x} \in \mathbb{R^n}$

$$
\vec{x} =
\begin{bmatrix}
	x_1\\
	x_2\\
	\vdots\\
	x_n
\end{bmatrix}
$$

to the hidden layer vector $\vec{h} \in \mathbb{R^h}$

$$
\vec{h} =
\begin{bmatrix}
	h_1\\
	h_2\\
	\vdots\\
	h_h
\end{bmatrix}
$$

And the transformation $T_2: \mathbb{R^h}	\rightarrow \mathbb{R^m}$ maps the hidden layer vector $\vec{h} \in \mathbb{R^h}$ to the output layer vector  $\vec{y} \in \mathbb{R^m}$

$$
\vec{y} =
\begin{bmatrix}
	y_1\\
	y_2\\
	\vdots\\
	y_m
\end{bmatrix}
$$

The transformations $T_1$ and $T_2$ are represented by matrices $W_1$ and $W_2$ of randomly generated weights.

$$
\begin{align}
W_1 = \begin{bmatrix}
	w_{1,1} & w_{1,2} & \ldots & w_{1,n}\\
	w_{2,1} & w_{2,2} & \ldots & w_{2,n}\\
	\vdots & \vdots & \ddots & \vdots\\
	w_{h,1} & w_{h,2} & \ldots & w_{h,n}\\
	\end{bmatrix}

T(\vec{x}) = W\vec{x} = \vec{s}
\end{align}
$$

and

$$
\begin{align}
W_1 = \begin{bmatrix}
	w_{1,1} & w_{1,2} & \ldots & w_{1,n}\\
	w_{2,1} & w_{2,2} & \ldots & w_{2,n}\\
	\vdots & \vdots & \ddots & \vdots\\
	w_{h,1} & w_{h,2} & \ldots & w_{h,n}\\
	\end{bmatrix}

T(\vec{x}) = W\vec{x} = \vec{s}
\end{align}
$$


And $W_2$ is represened by an $mxh$ matrix where $h$ is the number of elements in the hidden layer and m is the number of elements in the output layer.

$$
\begin{align}
T: R^n\rightarrow R^m\\
T(\vec{s}) = W_h\vec{s} = \vec{y}
\end{align}
$$


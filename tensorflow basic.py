import tensorflow as tf 


## session
m1=tf.constant([[2,2]])
m2=tf.constant([
    [3],
    [3]
])

dot_operation=tf.matmul(m1,m2)

init=tf.OptimizerOptions()

sess=tf.Session()
result=sess.run(dot_operation)
print(result)
sess.close()

with tf.Session() as sess:
    result_=sess.run(dot_operation)
    print(result_)


## placeholder
x1=tf.placeholder(tf.float32,shape=None)
y1=tf.placeholder(tf.float32,shape=None)
z1=x1+y1

x2=tf.placeholder(tf.float32,shape=[2,1])
y2=tf.placeholder(tf.float32,shape=[1,2])
z2=tf.matmul(x2,y2)

with tf.Session() as sess:
    z1_value=sess.run(z1,feed_dict={x1:1,y1:2})
    z2_value=sess.run(z2,feed_dict={x2:[[2],[2]],y2:[[3,3]]})
    print(z1_value)
    print(z2_value)

    z1_value,z2_value=sess.run([z1,z2],
    feed_dict={
        x1:1,y1:2,
        x2:[[2],[2]],y2:[[3,3]]
    })
    print(z1_value)
    print(z2_value)


## variable
var=tf.Variable(0)

add_operation=tf.add(var,1)
update_operation=tf.assign(var,add_operation)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(3):
        sess.run(update_operation)
        print(sess.run(var))


## activation
import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-5,5,200)
y_relu=tf.nn.relu(x)
y_sigmoid=tf.nn.sigmoid(x)
y_tanh=tf.nn.tanh(x)
y_softplus=tf.nn.softplus(x)
y_softmax=tf.nn.softmax(x)

sess=tf.Session()
y_relu,y_sigmoid,y_tanh,y_softplus,y_softmax=sess.run([y_relu,y_sigmoid,y_tanh,y_softplus,y_softmax])

plt.figure(1,figsize=(8,6))
plt.subplot(221)
plt.plot(x,y_relu,c='red',label='relu')
plt.ylim((-1,5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x,y_sigmoid,c='red',label='sigmoid')
plt.ylim((-0.2,1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x,y_tanh,c='red',label='tanh')
plt.ylim((-1.2,1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x,y_softplus,c='red',label='softplus')
plt.ylim((-0.2,6))
plt.legend(loc='best')

# plt.figure(1,figsize=(8,6))
# plt.subplot(111)
# plt.scatter(x,y_softmax)

plt.show()


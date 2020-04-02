# CLOUD-COMPUTING-CLASS-2020-Lab6
## Programming your cloud infrastructure

Participant Members:
* Ishaan Dwivedi
* Anant Gupta

*Objective*: To implement and understand the working of `load balancer` along with `auto-scaling` while deploying applications on the cloud.

## Task 6.1 Bootstrap the creation of your web server

'Load balancing' refers to efficiently distributing incoming network traffic across a group of backend servers, also known as a server farm or server pool. It sits in front the servers and ensures no particular server is overworked or incase of a particular failure, traffic is re-routed to the others.

'Auto-scaling' as the name suggests is a way to automatically scale up or down the number of compute resources that are being allocated to your application based on the traffic it encounters at any given time. 

Best usage of load balancing is when used in parallel with auto-scaling, since in absence of the latter, you’ll have to know ahead of time how much capacity you need so you can keep additional instances running and registered with the load balancer to serve higher loads. 


### Questions
#### Q611. What happens when you use https://your-load-balancer-url instead of http://your-load-balancer-url ? Why does that happen? How could you fix it?
`Answer:` When trying to use the HTTPS link, the browser throws an Invalid Certificate Error as shown in the screenshot below. This happends due to the fact that we are using a self-generated SSL certificate that the browser uses as a means to identify a secure connection. This can be fixed by purchasing a certificate that allows the browser to assure the security of the connection.

#### Q612. Stop all three EC2 instances and wait aprox. 5 minutes. What happens? Why?
`Answer:`

#### Q613. Terminate all three EC2 instances and wait aprox. 5 minutes. What happens? Why?
`Answer:`

#### Q614. How are you going to end this section regarding the use of AWS resources?
`Answer:`

#### Q615. Create a piece of code (Python or bash) to reproduce the above steps required to launch a new set of web servers with a load balancer. Start using the AMI that you have already created.
`Answer:`


## Task 6.2: Serverless example

### Questions
#### Q621. What is the list of events that the above URL triggers?
`Answer:`

#### Q622. Does the reply of the above URL match what it should be expected? Why?
`Answer:`

#### Q623. Explain what happens (actions and parts activated) when you type the URL in your browser to obtain the page updated with the shopping list.
`Answer:`

#### Q624. Explain what happens (actions and parts activated) when you type a new item in the New Thing box.
`Answer:`



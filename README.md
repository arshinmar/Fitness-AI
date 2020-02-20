# Fitness Buddy (FitBud)
This repository was created for the MakeUofT hackathon on February 15-16, 2020. 

### Team

The team consists of Arsh Kadakia, Sepehr Hosseini, Ben Natra and Nicola Lawford.

### Result

This submission received a top 5 placement at the hackathon amongst a pool of 240 participants from universities all across Canada.

### Inspiration:

It is difficult for university students to find the time and money to go to the gym. Although some YouTube videos teach exercises that can be done at home without weights, it's not always easy to self-correct without a gym buddy.

### What it Does:

When a user works out at home, they can place their laptop camera and display at the front of their space. They carry an Arduino microcontroller in their pocket and tape a haptic motor to their wrist or side. They select from a list of exercises--so far we have implemented tricep pushups and squats--and computer vision is used to detect form errors. The haptic motor alerts the user to form errors, so they know to look at the screen for feedback. These are the implemented feedback items: TRICEP PUSHUPS:

• Move wrists closer together or farther apart such that they are under the shoulders
• Keep elbows tucked in through the pushup SQUATS:
• Go lower
• Keep knees directly above ankles, not too far forward
• Sit more upright with a straight back
 
### How We Built It

We used a pretrained implementation of CMU Posenet in Tensorflow (link) for pose estimation. We analyzed coordinates of joints in the image using our own Python functions based on expert knowledge of workout form. The vision processing feedback outputs from the laptop are interfaced to an Arduino Uno over Bluetooth connection, and the Uno controls a Grove haptic motor.

### Challenges We Ran Into

• Diagnosing physical hardware problems: We spent a lot of time debugging a Raspberry Pi with a faulty SD card. We learned that it's important to debug from the hardware level up.

• Finding usable TensorFlow models that fit well to our mission. We got a lot better at filtering usable sources and setting up command line environments.

• Creating a durable and wearable design of the fitness buddy. We experienced issues with haptic motor connector wires breaking as we exercised. We learned the importance of component research in planning physical designs.

### Accomplishments that We're Proud of

• Integrating Python and Arduino using a Bluetooth module to achieve haptic feedback.

• Labelling joints and poses for analysis through appropriate machine learning models.

• Adding analysis to machine learning outputs to make them useful in a real life context.

• Learning to use different languages and products (including Raspberry Pi) to perform specific technical tasks.

### What We Learned

• How to use many different hardware products and techniques, including a bluetooth module, haptic motors and controllers, and a Raspberry Pi (which we did not use in our final design). 

• The efficiency and output derivation of many different machine learning models.

• The importance of prototyping physical systems that people will interact with and could break.

• A greater sense of focus towards better wellbeing of individual people through exercise.

### What's Next for Fitness Buddy: Haptic Feedback on Exercise Form:

• Incorporate and add software for a variety of different exercises.

• Migrate to Raspberry Pi for a more portable experience.

• Integrate with Google Home for more seamless IoT ("Ok Google, start my pushup routine!").

• Add goal setting and facial recognition for different household users with different goals.

### Questions?

Contact Arsh Kadakia or Sepehr Hosseini (collaborators on this repository) for further details.

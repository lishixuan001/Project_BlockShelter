# BlockShelter    
       
Possible Usage: Adjunct to Google Maps     
      
# To try out as a user    
For User interface, run gui_login.py.      
You should be able to keep going in the "search destination" path.    
For destination, there is a sample destination called "sample".     
You should be able to explore the use of this software by trying up.   
The "Find the Path" functionality is not available in this version, since the format of the maps    
havan't been finally determined. However, it is likely to be developed soon with APIs.    
        
# To try out as a Admin    
For Admin interface, run gui_back_end_login.py   
Another tricky way to access Admin Login page is to type "admin_login" in users' login page   
      
# More
There are actually more hidden interesting facts to be explored, try it out!     
       
# Inspiration
Sometimes in large cities or in some busy bu crowded places, people suffer a lot while looking for a parking lot. There is little information that guides people to available parking spaces. We hope to assemble the resources in parking lots, make databases, and guide people to the best-choice parking lot. The idea can be part of the Google Maps.

# What it does
It mainly has two functionalities. Firstly, it collects information for parking lots that are open to public, which includes the parking-lot map, and a system that keep tracks of the changes in available spots in each parking lot. The database for each parking lots place is in a local network system. Whenever a user is near the networks (can detect the network signals), they can get information about where can they find a spot in the parking lots(usually only the number of empty spots are shown, but people sometimes just have a hard time finding it). People can search for the destination, and then recommended parking places will be shown. Secondly, we assemble all parkable resources, and allow people who hope to rent out there own parking space to do so. Many people have their own parking lots, but they don't use them until they get back home. During the daytime, they can choose to put their parking lots available to the public. The public can park on the spots after paying some money. This really helps in cities where there are communities in the busy and crowded city.

# How I built it
It is built by python, basically package tkinter. All the materials are in python system, including the database system. It is really efficient to have local network sharing the information since there is usually little signal under most parking lots.

# Challenges I ran into
There should be a Admin end for the database management, a database in the middle that stores all the value, and a users' end that get info from the database through some interface. This connection is little hard since we need to visualize every data clearly and manage them correctly.

# Accomplishments that I'm proud of
I learned the related python package in one night. I spent most time in workshops for ideas and opportunities thus I started really late. But anyway I almost finished the structure and the interface. There are many little interesting things in the software, such as some secret code that can induce special interfaces. I love it!

# What I learned
Python's packages, and use python to make interactive database management. I really experienced the excitement to develop from back end to front end.

# What's next for BlockShelter
We should try to make everything get out of the limit of the local network things. We will do more APIs for the software, and try to better the contract for the private parking lots sharing process. We will need more actually situations rather than mostly demos


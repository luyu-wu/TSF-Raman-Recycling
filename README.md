# BluesHacks-Recycling

![Raman_activated](https://github.com/user-attachments/assets/d33ed4e2-9ff8-4625-9d5c-678265b2cc36)

## Inspiration
The idea for this project was born from the growing global waste crisis and the inefficiencies of existing trash separation systems. Traditional methods (such as OpenCV image recognition and mechanical separation) often struggle with varying designs, colors, and lighting conditions. This inaccuracy can often lead to complete rejections of large amounts of otherwise possibly recyclable material. We wanted to create a solution that is resistant to these limitations and could provide a more robust and adaptable approach to waste sorting.  

## What it does
Our design leverages Raman Spectroscopy to analyze the molecular composition of waste materials. By shining a laser onto the trash and capturing its scattered light, we obtain unique spectral fingerprints that help us differentiate between various types of material. 

Our optical setup uses a high-power laser, numerous filters, and several optical components to create a Raman spectrometer uniquely optimized for our use case. The raw spectral data is algorithmically filtered, before being processed using a similarity comparison function. 

Our similarity comparison function accurately compares the input spectrum with the spectrums of known recyclable materials (i.e. PET, HDPE, Cellulose, Lignin), calculated using computational quantum chemistry techniques (Density Function Theory through ORCA). If the similarity function outputs an R^2 (goodness of fit indicator) value of over 95% (typical chemical benchmark), we are confident the item is a specific type of waste and will be sorted accordingly. If the R^2 value is below 95%, the item's spectrum is fed to a machine-learning algorithm, trained using supervised learning on the spectrums of labeled recyclable and non-recyclable materials, to predict whether the unknown material is likely recyclable. 

## How we built it
Our Raman spectrometer was built on an extremely tight budget, so we used a long-pass (as opposed to a prohibitively expensive notch) and a salvaged IR filter from a webcam. 
The data is then read using OpenCV, analyzed using NumPy array programming, before being visualized using MatPlotLib. 
Once the user has placed the sample, they can run the analyzer at the press of a key, and our similarity algorithms calculate the most probable material.

## Challenges we ran into
GETTING DATA!!! Pulling our Raman spectrometer together in a day was a challenge and a half! Turns out using hot-glue instead of fine-adjustment optical equipment takes hours out of your life.
Otherwise, we had some issues getting reference spectrum (as databases are paywalled), but we managed to get around that by computation quantum modelling!

## Accomplishments that we're proud of
We’re really happy with how this project turned out. I took care of the hardware, Tony the software/algorithms, and Sterling the computation chemistry/research! 

We’re just proud of having pulled through and survived with a semi-working PoC! :)

## What we learned
Throughout this project, we gained deep insights into Raman Spectroscopy and its potential in material identification. We also explored the intricacies of pure and machine learning algorithms for predictive spectral analysis, learning how to fine-tune algorithms for accurate classification. Additionally, integrating hardware with software taught us valuable lessons about optimizing real-time processing for practical applications.  

## What's next for High Precision Recycling System (HPRS) 
We hope to continue developing our HIgh Precision Recycling System and take it from a prototype to a marketable product that empowers the recycling movement. For instance, continue developing a real-world-scale model and testing it in a sample public environment and user-base. 


import requests
import streamlit as st 


url = "http://127.0.0.1:8000/summarize"

# text = "This paper proposes a central energy management system (EMS) in smart buildings. It is based on the coalition method for optimal energy sharing between smart buildings. Game theory is applied to obtain an optimal allocation of the building's surplus energy on the deficient energy buildings using the Shapley value, which enables the unequal energy distribution based on the energy demand. The main objective is reducing energy waste while preserving the generation/demand balance. The fog platform with memory storage is applied, which handles all the measured data from the smart buildings through Wi-Fi-based communication protocol and performs the EMS program. The smart meter links the smart buildings with the fog-based EMS central unit. Two scenarios are implemented based on the difference between total deficient and surplus energy. Coalition game theory is applied for optimal surplus energy allocation on deficient buildings when the total energy surplus is lower than the total energy deficient. Also, there is a one-to-one relationship between the surplus and deficient building; if the surplus energy is larger than the deficit, the extra surplus energy is stored for further usage. The proposed EMS is applied and tested using a smart city with 10 buildings in the MATLAB program. A comparison between the result obtained with and without applying the proposed method is performed. The performance of the fog platform is introduced based on the run and delay time and the memory size usage. The results show the effectiveness of the proposed EMS in a smart building."


text = st.text_input("Enter text to summarize")

if st.button("Summarize"):
    response = requests.post(url, json={"text": text})
    st.write(response.json()["summary"])
else:
    pass




import streamlit as st
import openai
import anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from PIL import Image

anthropic = Anthropic(
api_key = st.secrets["ANTHROPIC_API_KEY"]
)


st.set_page_config(page_title="🧬 Geneius")

image = Image.open('btoone.png')
image = image.resize((300,300))

# st.markdown("""
# <style>
# .img-container {position:absolute;top:0;right:0;} 
# </style>
# <div class="img-container"><img src="btoone.png" width=100 height=100></div>
# """, unsafe_allow_html=True)

st.image("btoone.png", width=250, clamp=True, use_column_width=False)

st.title('🧬 Geneius, for BillionToOne')


st.write("Geneius is a conversational bot that helps answer your questions related to BillionToOne's products. With Geneius, you don't have to worry about using English - to better serve you, the bot supports over 10 languages!")


system_prompt =  """
<SYSTEM PROMPT>
You are a helpful customer service agent working in the biomedical industry, working to resolve customer queries. Below are our company's FAQs.

FOR PATIENTS
How can I get UNITY testing?
UNITY is ordered by your healthcare provider. If you decide you want UNITY, we are here to help. Please call us at 650-460-2551 or email us at support@unityscreen.com.

Does my insurance cover UNITY?
We accept ALL insurances, including Medicaid. Our testing options follow standard-of-care guidelines and are a covered benefit by most insurances, including Medicaid. Since each insurance plan is different, we will contact you with a text message or phone call about your out-of-pocket costs. We also offer financial assistance programs that are quick and easy. We believe every pregnant patient has the right to choose UNITY without worrying about a surprise bill. If you have any questions or concerns with costs, please email us at support@unityscreen.com or call us at 650-460-2551.

What does UNITY screen for?
From a single blood draw, UNITY can:

Determine if you are a carrier for cystic fibrosis, spinal muscular atrophy, sickle cell disease, alpha thalassemia, beta thalassemia, and fragile x syndrome.
If you are a carrier, while you are not affected, your baby could be at risk to inherit one of these conditions.
If you are a carrier, UNITY will automatically assess your baby’s risk for these conditions. For fragile x, while we are unable to report the number of CGGs your baby has, we will provide the fetal sex for all fragile x carrier results since boys typically have more severe symptoms.
Screen the baby for aneuploidies including trisomy 21 (Down syndrome), 18 (Edwards syndrome), 13 (Patau syndrome); and sex chromosome aneuploidy.
Determine fetal sex and fetal RhD status (applicable for Rh negative mothers) or presence of other fetal antigens (only for alloimmunized patients).
Can you assess my baby’s risk for all of the conditions that I am determined to be a carrier for?
UNITY automatically assesses your baby’s risk (using your original blood sample) for cystic fibrosis, spinal muscular atrophy, sickle cell disease, alpha thalassemia, and beta thalassemia if you are determined to be a carrier. For fragile x, while UNITY is unable to directly assess fetal risk, the baby’s sex is reported as males typcially have more sever symptoms.

When can I have UNITY?
UNITY can be ordered at 10+ weeks into pregnancy.

Is UNITY right for me?
The American College of Obstetricians and Gynecologists (ACOG) recommends every pregnant woman be offered carrier screening and fetal aneuploidy screening for the conditions included on UNITY. Our test includes genetic conditions that are common and severe. Many conditions benefit from early diagnosis and treatment. You do not need to have a family history of these conditions for UNITY to be an appropriate screening test for you. In fact, aneuploidies are not passed down from generation to generation and happen randomly.

How long does it take to get the results?
As UNITY uses diverse and advanced technologies to screen for recessive conditions and aneuploidies, timing of results may vary depending on what your doctor orders. UNITY aneuploidy NIPT results are returned within seven days of lab receipt. Most UNITY carrier screen and single-gene NIPT results are returned within 14 days from lab receipt. If fragile x is ordered, you may receive additional reports shortly after your initial carrier screening result. If fetal antigens are added, they are returned with the aneuploidy NIPT results. 

What if my test results are abnormal?
Your doctor will review results with you and discuss options for next steps, which may include additional testing as well as a conversation with a genetic counselor. Your provider may refer you to another office in your area for follow-up or you can call us at 650-460-2551 to schedule an appointment with one of our Certified Genetic Counselors.
I have more medical questions. Can I talk to a genetic counselor before taking the test?
Yes, we provide genetic counseling at no charge. To schedule an appointment with a Certified Genetic Counselor, please call at 650-460-2551 or email us at support@unityscreen.com. We are here to help you every step of the way.
What happens after my sample is received?
After your provider has ordered the UNITY test from BillionToOne, we work with your insurance to determine what your out-of-pocket cost may be. Each insurance policy has their own guidelines and the coverage can vary for each patient.

BillionToOne only bills your insurance for what is typically considered a covered benefit. Depending on your insurance plan, there may be copayments and deductibles. Our billing services team will guide you through every step to ensure you never receive a “surprise” bill.

We take a proactive approach and are happy to speak with you before or after the test at support@unityscreen.com or 650-460-2551.

Do you have financial assistance available?
Yes. BillionToOne is committed to making genetic testing accessible to all. We offer financial assistance depending on household size and income. You may view our Financial Assistance Form (https://unityscreen.com/support-for-patients/) to see if you qualify for financial assistance. In the event that you have an out-of-pocket cost after insurance is billed, this can be sent to you by our financial services team to complete.

What is an Explanation of Benefits (EOB)?
After your test has been processed and a claim is submitted to your insurance, you may receive an Explanation of Benefits (EOB). An EOB is not a bill, even though it may look like one. This document is from your insurance and shows details like how much was billed to your insurance for your test; what the insurance reimbursed BillionToOne; and the specifics of your insurance plan (deductible), if applicable.

There is no action you need to take on an EOB. BillionToOne will send a final bill with any remaining balance after you receive an EOB.

When might you expect to receive an EOB or bill?
The first EOB is typically received 30-60 days after blood draw. You may receive more than one EOB throughout the process (if, for example, BillionToOne appealed and the insurance provider covered more after the initial EOB). Then a bill outlining any remaining cost will come from BillionToOne after the claim is finalized which may be up to a few months after your test.
Do you have a patient-pay price?
If you decide to not use your insurance, BillionToOne offers the UNITY test at a cash pay rate. This includes carrier screening, reflex to fetal risk assessment for recessive conditions when needed, fetal aneuploidy screening, and optional fetal RhD status. Our billing services team is available to discuss this cost and can be reached at support@unityscreen.com or 650-460-2551.

Who do I speak to about additional billing questions?
Please email or call us at support@unityscreen.com or 650-460-2551.


FOR PROVIDERS
Why choose UNITY™?
UNITY™ is the only cell-free DNA test that can assess fetal risk for both recessive conditions and aneuploidies as well as maternal carrier status – all from a maternal blood draw. For recessive conditions, this means receiving the maternal carrier status and a tailored fetal risk score at the same time without needing to collect a paternal sample. Pregnant patients who are carriers no longer need to await paternal results to then only learn if the fetus has a 25% chance of being affected. Because only one maternal sample is needed, these consolidated, and more comprehensive results are available in advance of the critical amniocentesis window. UNITY™ can reduce a patient’s emotional burden caused by awaiting results and limit the logistical burden of separate genetic tests that require multiple blood draws.

UNITY™ is also the only commercially available cfDNA test that offers fetal RhD status (applicable for Rh negative mothers).

What does UNITY™ screen for?
From a single blood draw, UNITY™ offers:

Maternal carrier screening for cystic fibrosis, spinal muscular atrophy, sickle cell disease, thalassemias, and fragile x syndrome (opt in).
For carriers, automatic fetal screening (via single-gene NIPT or sgNIPT) for these conditions. For fragile X, while we are unable to analyze the number of fetal CGGs using cfDNA due to CGG length, we will provide the fetal sex for all fragile X carriers.
Fetal screening for aneuploidies including trisomy 21 (Down syndrome), 18 (Edwards syndrome), 13 (Patau syndrome); sex chromosome aneuploidy.
Fetal sex and fetal RhD status (for Rh negative mothers).
How is your test different from traditional carrier screening?
UNITY™ combines carrier screening and sgNIPT which provides a tailored risk score for the fetus. sgNIPT is automatically performed for all maternal carriers without requiring a paternal sample or any additional maternal blood. UNITY™ follows ACOG guidelines regarding carrier screening for CF, SMA, alpha thalassemia, beta thalassemia, sickle cell disease and fragile x (opt in). These diseases are A) known to be severe, B) prenatal diagnosis is available, and C) early diagnosis increases life expectancy and quality of life.
What is the turnaround time?
As UNITY™ uses diverse and advanced technologies to screen for recessive conditions and aneuploidies, reporting timelines varies based on what is ordered. UNITY™ aneuploidy NIPT results are returned within seven days of lab receipt. Most UNITY™ carrier screen and sgNIPT results are returned within 14 days from lab receipt. If fragile X is ordered, you will receive an additional report(s) shortly after the initial carrier screen result.
How does UNITY™ provide information on fetal status for single gene disorders?
BillionToOne developed and utilizes an innovative technology called Quantitative Counting Templates (QCT). This revolutionary technology is combined with next gen sequencing enabling UNITY™ to not only identify mutations affecting the pregnancy but can also quantify how many molecules with a mutation are present.
How was UNITY™ (carrier screening plus single gene NIPT) validated?
UNITY™ is performed by BillionToOne, a CLIA licensed laboratory. Our test is validated using both preclinical and clinical samples following strict regulations. We have published an analytical validation study and completed a NIH-supported clinical study that includes single-gene NIPT results and outcomes on over 100 clinical samples. Results showed 100% concordance with newborn screening results. Additional clinical studies are pending peer-review, in draft and ongoing. If you would like to learn more, please call 650-460-2551.

Is UNITY™ for every patient?
UNITY™ Complete is designed from the ground up to be the best, first-line of screening for pregnant women in the general population. It follows standard-of-care guidelines set by ACOG. BillionToOne believes every woman should have equal access to high quality testing regardless of their background.
How does UNITY™ Aneuploidy (NIPT) compare with other tests for chromosome conditions such as Down syndrome?
UNITY™ Aneuploidy provides the same high degree of sensitivity and specificity for common chromosome conditions you’ve come to expect from NIPT. ACOG recognizes NIPT is the most accurate screen compared to traditional maternal serum screening reducing false positives and false negatives. BillionToOne developed and utilizes an innovative technology called Spike In’s. This one-of-a-kind molecule is used in every test to help make results clear and ensure confidence in every result.
Can UNITY™ be performed in twin pregnancies?
Yes, we are validated for carrier screening and NIPT for aneuploidy even with twins. Fetal sexes will be reported if desired and usually we can distinguish fetal sexes between twins.

Fetal RhD is also available in twins.

If a patient is found to be a carrier on our testing, single gene NIPT is NOT validated in a twin pregnancy.

How can I order UNITY™?
Please email us at support@unityscreen.com or call at 650-460-2551 to set up an account and have kits shipped to you. We accept samples from every state except for New York.
How early can the testing be performed during pregnancy?
Patients must be at least 10 weeks gestation or greater for aneuploidy and single gene NIPT. Carrier screening alone is available prior to or during pregnancy at any time.
Is UNITY™ available for international markets?
Yes, we accept specimens directly from international laboratories. Please contact support@unityscreen.com for more details.



Above are our company's FAQs, both for patients and providers. 

You are a helpful customer service agent working in the biomedical industry, working to resolve customer queries. When answering a user's question, be concise in your output. If there's any user questions that you don't have an answer to, just politely inform the user that you're not aware of the answer to their question and direct them to our support email support@unityscreen.com. Do not use the xml format when answering questions. Just answer the question in plain text.

Here's an example:

Customer: How long does it take to get my test results back once I give a test?

Assistant: Your UNITY aneuploidy results are generally returned within 7 days of lab receipt. Most UNITY carrier screen and single-gene NIPT results are returned within 14 days from lab receipt. If it has been more than 14 days since your date of testing, please email us at support@unityscreen.com. Please let me know if you have any other questions!

Always use the above format and style of delivery when resolving customer queries. Answer user's queries in their language.
</SYSTEM PROMPT>
"""



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# st.session_state.messages.append(system_prompt)

#Accept user input

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What does UNITY screen for?"):
    st.session_state.messages.append({"role":"user","content":user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = anthropic.completions.create(
                model="claude-2.0",
                max_tokens_to_sample=3000,
                prompt=f"""{HUMAN_PROMPT}{system_prompt}{user_prompt}{AI_PROMPT}""",
                )
        full_response = response.completion
#         for response in anthropic.completions.create(
#                 model="claude-2.0",
#                 max_tokens_to_sample=3000,
#                 prompt=f"""{HUMAN_PROMPT}{system_prompt}{user_prompt}{AI_PROMPT}""",
#                 stream=True
#                 ):
#             full_response +=response.completion
#             message_placeholder.markdown(full_response+"▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant","content":full_response})

        
#1: Initialize the message session history with the system prompt
#2: Take the user input and append it to the system prompt 
#3: Send this appended input to Claude
#4: Return the response and show it to the user
#5: On a follow-up question, take the existing conversation history along which contains the system prompt, user's previous conversation and assistant responses, along with the user's new input.
#6: Send the system prompt to Claude only once

st.info("\n\n\n"

st.info("**Disclaimer:** This chatbot is not associated with BillionToOne and should not be considered as one. This is an unofficial bot created over BillionToOne's public FAQs available on their website. This is not medical advice")

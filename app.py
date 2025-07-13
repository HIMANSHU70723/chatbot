import streamlit as st

# Financial data
financial_data = {
    "Microsoft": {
        "Total Revenue": 64773,
        "Net Income": 88136,
        "Net Income Change (%)": 21.80
    },
    "Tesla": {
        "Total Revenue": 96773,
        "Net Income": 14997,
        "Net Income Change (%)": 19.44
    },
    "Apple": {
        "Total Revenue": 383285,
        "Net Income": 97400,
        "Net Income Change (%)": -2.41
    }
}

# Chatbot logic
def financial_chatbot(query):
    query = query.lower()

    if "total revenue" in query:
        return (
            f"📊 **Total Revenue:**\n"
            f"- Microsoft: ${financial_data['Microsoft']['Total Revenue']} million\n"
            f"- Tesla: ${financial_data['Tesla']['Total Revenue']} million\n"
            f"- Apple: ${financial_data['Apple']['Total Revenue']} million"
        )
    elif "net income change" in query or "how has net income changed" in query:
        return (
            f"📈 **Net Income Change (YoY):**\n"
            f"- Microsoft: {financial_data['Microsoft']['Net Income Change (%)']:.2f}%\n"
            f"- Tesla: {financial_data['Tesla']['Net Income Change (%)']:.2f}%\n"
            f"- Apple: {financial_data['Apple']['Net Income Change (%)']:.2f}%"
        )
    elif "net income" in query:
        return (
            f"💰 **Net Income:**\n"
            f"- Microsoft: ${financial_data['Microsoft']['Net Income']} million\n"
            f"- Tesla: ${financial_data['Tesla']['Net Income']} million\n"
            f"- Apple: ${financial_data['Apple']['Net Income']} million"
        )
    else:
        return "❌ Sorry, I can only answer predefined queries like total revenue, net income, or net income change."

# Streamlit UI
st.set_page_config(page_title="Financial Chatbot", page_icon="🤖")
st.title("🤖 Financial Chatbot")
st.markdown("Ask about **Total Revenue**, **Net Income**, or **Net Income Change**.")

user_input = st.text_input("Type your question:")

if user_input:
    response = financial_chatbot(user_input)
    st.markdown(response)

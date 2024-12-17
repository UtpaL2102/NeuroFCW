import streamlit as st
import json

def main():
    st.set_page_config(page_title="FCW System Requirements", layout="wide")

    # Sidebar with instructions and prompt summary
    st.sidebar.header("Instructions")
    st.sidebar.write(
        "1. Prompt the FCW system requirements in the text box provided.\n"
        "2. Use the 'Set Parameters' button to add custom parameters.\n"
        "3. Use the 'System Parameters' button to view and modify pre-set parameters."
    )

    if 'parameters' not in st.session_state:
        st.session_state.parameters = []
    if 'user_prompt' not in st.session_state:
        st.session_state.user_prompt = ""

    # Display overall prompt in JSON format
    def update_sidebar():
        prompt_summary = {
            "task": st.session_state.user_prompt,
            "parameters": {param[0]: param[1] for param in st.session_state.parameters}
        }
        st.sidebar.header("Prompt Summary")
        st.sidebar.code(json.dumps(prompt_summary, indent=4))

    # Main Title
    st.title("Forward Collision Warning (FCW) System Requirements")

    # User input for FCW system requirements
    st.session_state.user_prompt = st.text_area(
        "Enter the requirements for the FCW system:",
        placeholder="Write code for FCW system...",
        value=st.session_state.user_prompt
    )

    # Buttons for parameter settings
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Set Parameters"):
            st.write("Add custom parameters below:")

            # Initialize the parameters list in session state
            if 'parameters' not in st.session_state:
                st.session_state.parameters = []

            # Temporary storage for current input
            if 'current_param_name' not in st.session_state:
                st.session_state.current_param_name = ""
            if 'current_param_value' not in st.session_state:
                st.session_state.current_param_value = ""

            # Input fields for Parameter Name and Parameter Value
            st.session_state.current_param_name = st.text_input(
                "Parameter Name:", value=st.session_state.current_param_name, key="current-param-name"
            )
            st.session_state.current_param_value = st.text_input(
                "Parameter Value:", value=st.session_state.current_param_value, key="current-param-value"
            )

            # Button to add the parameter
            if st.button("Add Parameter"):
                if st.session_state.current_param_name and st.session_state.current_param_value:
                    # Append the parameter to the session state
                    st.session_state.parameters.append(
                        (st.session_state.current_param_name, st.session_state.current_param_value)
                    )
                    # Clear the input fields for the next parameter
                    st.session_state.current_param_name = ""
                    st.session_state.current_param_value = ""
                else:
                    st.warning("Please fill both Parameter Name and Parameter Value fields.")

            # Display the list of added parameters
            for param_name, param_value in st.session_state.parameters:
                st.write(f"- {param_name}: {param_value}")


    with col2:
        if st.button("System Parameters"):
            st.write("Modify system parameters below:")
            odd_model = st.text_input("ODD Model", value="Yolo11")
            ttc = st.number_input("Time to Collision (TTC)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
            threshold_distance = st.number_input(
                "Threshold Relative Distance (m)", min_value=0.1, max_value=10.0, value=2.0, step=0.1
            )
            threshold_speed = st.number_input("Threshold Relative Speed (m/s)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
    update_sidebar()

if __name__ == "__main__":
    main()

# 🚀 **NeuroFCW - Neural Network-Based FCW System**
**Author - Aryan Pandey, Priyadarshi Utpal and Sanket Poojari**

NeuroFCW is an innovative **Forward Collision Warning (FCW)** system that leverages **Generative AI** and **Neural Networks** for automated FCW code generation, test case validation, and continuous improvement. 

---

### 📊 **System Architecture**

Below is the high-level system architecture overview for **NeuroFCW**:

![System Architecture](fcw.jpg)

---

### 🧠 **Key Features**
1. **Document Processing**  
   - Segments input documents into manageable chunks for LLM-based processing.

2. **Knowledge Base Integration**  
   - Stores and retrieves safety standards, MISRA guidelines, test cases, and code examples using **Neo4j Graph Knowledge Base**.

3. **Graph-RAG Code Generation**  
   - Generates FCW code compliant with MISRA standards using:
     - Contextual data retrieval
     - Code generation with a **Large Language Model (LLM) API**

4. **Graph-RAG Test Case Generation**  
   - Automatically generates comprehensive test cases with relevant test patterns.

5. **Fine-Tuned YOLO Model**  
   - Handles object detection and computes parameters for FCW validation.

6. **Validation & Continuous Improvement**  
   - Failed test cases are logged and used to improve future FCW code.

---

### 🛠 **Tech Stack**
- **AI/ML**: LangChain, YOLO (Object Detection)
- **Databases**: Neo4j, SQLite
- **Programming Languages**: Python
- **DevOps Tools**: Jenkins, GitHub
- **Frameworks**: Large Language Model APIs, Graph-RAG

---

### 📂 **System Workflow**
The system operates in the following steps:
1. **Input Documents** → Segmented into manageable chunks.
2. **Knowledge Base Processing** → Stores MISRA guidelines, safety standards, and examples.
3. **Code Generation** → LLM APIs generate compliant FCW code.
4. **Test Case Generation** → Retrieves patterns and validates with YOLO.
5. **Validation** → Test results logged, and the FCW system is updated continuously.

---

### ✅ **Output**
- **MISRA-Compliant FCW Code**
- **Comprehensive Test Cases**
- **Validated FCW Code Packages for Deployment**

---

### 📈 **Future Scope**
- Integration with real-time simulation environments.
- Enhanced model fine-tuning for edge cases.
- Expanded use cases for autonomous driving.

---

### 📷 **System Flowchart**
The full **System Architecture** flowchart is visualized below:

![NeuroFCW System Architecture](img/fcw.jpg)

---

### 🤝 **Contributors**
- Aryan Pandey
- Priyadarshi Utpal
- Sanket Poojari

---

### 🔗 **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/ltd-ARYAN-pvt/NeuroFCW.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main program:
   ```bash
   python app.py
   ```

---

### 🌟 **Contact**
For more information, reach me at:  
📧 **aryan2002pandeythrgrt@gmail.com**  

---
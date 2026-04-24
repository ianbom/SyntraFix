# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 1

- conversation_id: 12
- user_chat_id: 441
- bot_chat_id: 442

### user_input

Apa itu software engineering?

### retrieved_context

1. From SWEBOK ISO/IEC TR 1975:2015, we adopt the critical knowledge areas in software engineering to use as synonyms for software engineering. Twelve knowledge areas identified from the keywords were selected as most prevalent in the literature. These include software requirements, software design, software construction, software maintenance, software testing, software configuration management, software management, software process, software models and methods, and software quality. This is seen in similar SMSs in software engineering by other researchers Klotins et al. [40]. These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

2. Since the formulation of the term Search-Based Software Engineering (SBSE) [1], SBSE has attracted many research theories and applications. SBSE converts a software engineering problem into a computational search problem. The technique is based on the definition of the pool of possible solutions, which is known as the search space. Taking into account the complexity of modern software systems, the search space is too large to be explored exhaustively. To find a sufficiently good solution, SBSE follows the procedure that allows the selection of a potential solution from the search space based on given criteria. SBSE techniques (SBSET) have been applied at almost all the phases of the software development process starting from the requirement analysis [2], following software design, development, and refactoring [3], debugging and (The Acceptance of Search-Based Software Engineering Techniques: An Empirical Evaluation Using the Technology Acceptance Model, page 1)

3. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. Software engineering is a discipline that is concerned with various phases of software production from the preliminary requirement gathering stage through to maintenance of the software system. It is therefore concluded that software engineering is a discipline that leads to a systematic approach where cost effective software development is performed. Regardless of the speedy progress, the software industry is well thought-out by several to be in a crisis. At that time the average software projects exceed the schedule by half. Similarly, large number of projects were either not functioning as expected or were not used at all. There are numerous other challenges, industry needs to deal with, if it continued to step forward for much more mature engineering discipline. Varying situational contexts among team members are one of the many challenges that can lead to failure software if left unattended. Software engineering standards significantly acknowledge the importance of situational contexts. In this study we have investigated the IEEE standards association for the relevant standards. We found 32 most relevant stanafter performing filtration on the data set. We concluded that these software engineering standards significantly acknowledge towards consideration of situational contexts for successful software. Each standard is investigated for the various factors and sub-factors that can lead to varying situational contexts among software engineering team members. Based upon the analysis, we came across a pattern in the identified standards. We reported 8 categories under which these standards are grouped. Each of the standard reports the factors and sub-factors related to its category. The identified factors are 12 in number. Each of them is further grouped with the related sub-factors (52 in number) that ultimately can lead to failure software if not addressed properly. This study provides a guideline for the practitioners to consider these factors and sub-factors while performing software development in order to have a successful software development. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 11)

5. In pursuance of the issues raised from the empirical literature, it is necessary for process theory to transform software engineering body of knowledge especially paying attention to SSCs. Additionally, research in software engineering has been predominately prescriptive and method-focused [39], producing thousands of software development methods that remain underutilized. In order to solve the challenges with software practice, practitioners and researchers should contribute to the body of knowledge [135], given that SSCs dominate the industry and are responsible for over 80% of software produced in the market. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

6. Software requirements outline the purpose of the development and design. It serves as the foundation of software intended to develop [1]. Requirements are defined in the beginning and act as a developmental milestones to accomplish successful executable software components [2]. Software requirement engineering is a systematic approach that is significantly developed in the course of the most recent decade [3]- [5]. Software architecture can be viewed as an organization of a system that comprehensively includes components interactions, operational environments, design principles, software functionalities, and often covers future evolutionary software perspective [6]- [9]. (Integration of Software Architecture in Requirements Elicitation for Rapid Software Development, page 1)

7. A close look at the knowledge areas of software engineering used by the companies as reported in the selected articles indicates that general software development and project management are most prominent in the knowledge area frequency distribution, as presented in Figure 7.

The data detail specifically indicates the most covered knowledge area of software engineering by the articles selected in the study. Figure . 7, illustrates 3 most dominant knowledge areas presenting up to 46 studies identified on the knowledge areas of software development design and construction (33), project management ( 16), and quality (7). The remaining 31 studies covered the knowledge areas of process (5), models and methods (5), maintenance (4), testing (3), requirements (3) and management (1) with the respective number of studies. Although the knowledge areas that ultimately are observed at a point in time are presented decimally in the empirical literature, the initial 10 years show that these knowledge areas are not reflected in the empirical studies around this time. Figure 6(a) shows the studies in the years between 2016 and 2021 present interest in the knowledge area of quality, requirements, models and methods, and maintenance. Although the numbers are minimal, the growing interest of researchers is important for the industry and for the transformation of software development practice in SSCs. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 9)

8. The software engineering industry is undergoing a rapid transformation driven by the emergence of large language models (LLMs) and their use to create autonomous agents that can perform complex software engineering tasks. This paradigm shift, which we call agentic software engineering (ASE), represents a significant rethinking of how software is designed, developed, and maintained [1], [2], [3]. In contrast to traditional software engineering practices that rely primarily on human developers following established methodologies, ASE advocates the use of AI-based agents that have the autonomy to make decisions, write software, run tests, and interact throughout the software engineering lifecycle-a change reflected in recent work on LLM-based applications in software engineering [4], [5], [6], [7]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 1)

### response

Software engineering adalah suatu disiplin ilmu yang terkait dengan berbagai fase produksi perangkat lunak dari tahap pengumpulan kebutuhan awal hingga pemeliharaan sistem perangkat lunak.

### reference


---

## Sample 2

- conversation_id: 12
- user_chat_id: 443
- bot_chat_id: 444

### user_input

Bagaimana software engineering membantu meningkatkan software quality dan software maintenance?

### retrieved_context

1. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

2. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

3. Software analytics plays a major role in ASD and continuous software engineering since, properly used, the enormous amounts of data from different systems (e.g., continuous integration system, management tools, etc have proved increasingly useful for guiding (almost) real-time decisionmaking [31]- [33]. Indeed, companies like Microsoft are hiring data scientists for their software teams [34]. ASD and continuous software engineering have created numerous new opportunities for observing user behavior and monitoring how systems and services are being used; for identifying unexpected patterns and runtime issues; for monitoring system quality attributes; and for collecting real-time data to feed both business and technical planning [35], [36]. The main objective is to constantly monitor and measure both business indicators and infrastructure-related metrics in order to facilitate and improve business and technical decisionmaking [37]. In the specific case of software quality, continuous quality monitoring enables transparency to foresee, trace, and understand important aspects of product quality in real time [37], [38]. Support for product quality management is particularly relevant in ASD, since it tends to overlook quality aspects in favor of product functionality [17]. Although the literature reports on promising advances regarding the use of analytics in continuous software engineering [31]- [33], many challenges still exist, with the lack of software analytics tools being among the most relevant ones [32]. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

4. Software analytics plays a major role in ASD and continuous software engineering since, properly used, the enormous amounts of data from different systems (e.g., continuous integration system, management tools, etc have proved increasingly useful for guiding (almost) real-time decisionmaking [31]- [33]. Indeed, companies like Microsoft are hiring data scientists for their software teams [34]. ASD and continuous software engineering have created numerous new opportunities for observing user behavior and monitoring how systems and services are being used; for identifying unexpected patterns and runtime issues; for monitoring system quality attributes; and for collecting real-time data to feed both business and technical planning [35], [36]. The main objective is to constantly monitor and measure both business indicators and infrastructure-related metrics in order to facilitate and improve business and technical decisionmaking [37]. In the specific case of software quality, continuous quality monitoring enables transparency to foresee, trace, and understand important aspects of product quality in real time [37], [38]. Support for product quality management is particularly relevant in ASD, since it tends to overlook quality aspects in favor of product functionality [17]. Although the literature reports on promising advances regarding the use of analytics in continuous software engineering [31]- [33], many challenges still exist, with the lack of software analytics tools being among the most relevant ones [32]. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

5. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

6. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

7. Nowadays, a company's ability to innovate is increasingly driven by software. Digital technologies play a key role in The associate editor coordinating the review of this manuscript and approving it for publication was Waldemar W. Koczkodaj. the transformation of many industrial companies [1], especially in sectors like the automotive industry, where software (together with electronics) is responsible for over 90% of all innovations [2], [3]. In this context, software quality makes the difference and is an essential competitive factor for company success. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

8. Nowadays, a company's ability to innovate is increasingly driven by software. Digital technologies play a key role in The associate editor coordinating the review of this manuscript and approving it for publication was Waldemar W. Koczkodaj. the transformation of many industrial companies [1], especially in sectors like the automotive industry, where software (together with electronics) is responsible for over 90% of all innovations [2], [3]. In this context, software quality makes the difference and is an essential competitive factor for company success. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

Berikut adalah jawaban berdasarkan konteks:

Software Engineering (SE) dapat membantu meningkatkan software quality dan software maintenance dengan menggunakan teknik-teknik artificial intelligence (AI). Beberapa cara yang disebutkan dalam konteks termasuk:

* Menggunakan AI untuk mendeteksi potensi keamanan dan memberikan peringatan tentang masalah tersebut.
* Meningkatkan kemampuan analisis data untuk membantu pengembang membuat keputusan yang lebih baik.
* Menggunakan agen-agen otomatis untuk melakukan pemeliharaan software, seperti bug-fixing, refactoring, dan migrasi.

Selain itu, konteks juga menyebutkan bahwa software analytics sangat penting dalam meningkatkan kualitas perangkat lunak dan pemeliharaannya. Dengan menggunakan data dari berbagai sumber, pengembang dapat memahami perilaku pengguna, mengidentifikasi pola yang tidak terduga, dan mengoptimalkan kinerja sistem.

Jadi, jawaban singkat adalah: Menggunakan teknik-teknik AI dan software analytics untuk mendeteksi potensi keamanan, meningkatkan analisis data, dan menggunakan agen-agen otomatis untuk pemeliharaan software.

### reference


---

## Sample 3

- conversation_id: 12
- user_chat_id: 445
- bot_chat_id: 446

### user_input

Apa itu software quality?

### retrieved_context

1. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

2. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

3. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

4. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

5. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

6. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

7. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

8. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

Jawaban:
Software quality adalah totalitas sifat-sifat suatu entitas yang menentukan kemampuannya untuk memenuhi kebutuhan yang telah dinyatakan dan implisit.

(Sumber: [Source: Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study])

### reference


---

## Sample 4

- conversation_id: 12
- user_chat_id: 447
- bot_chat_id: 448

### user_input

Bagaimana software quality dinilai menggunakan software metrics dan software testing?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

3. The use of measurement is common in all aspects of human life such as scales for buying vegetables, fruits, grocery items, gold or making estimations for reaching to the home of a friend. The applications of measurement are obvious in all disciplines such as sciences, engineering, medical and others. The measurements play a vital role in software organizations for the improvement of software processes [1], [2]. It is reported by many software quality assurance agencies that the quality of software product is strongly influenced by the quality of software process followed to develop the software product [3]. Software measurement has become an essential process in software organizations for characterizing, evaluating, predicting and improving software products, processes, and resources [4]- [6]. ISO/IEC 15939:2007 [4] defines measurement process as ''a process for establishing, planning, performing and evaluating measurement within an overall project, enterprise or organizational measurement structure''. Despite the acknowledged importance and advocated benefits of measurement processes for software engineering community, their actual applications in the software industry are limited [4], [5], [8], [9]. It is also reported in a systematic review on measurements in software engineering that software process is the least measured entity [35]. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

4. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

5. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

6. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

7. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

8. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Berikut adalah jawaban berdasarkan konteks yang diberikan:

Software quality dapat dinilai menggunakan software metrics dan software testing melalui beberapa cara, seperti:

* Menggunakan metrik internal untuk mengukur kualitas sumber kode
* Menggunakan metrik eksternal untuk mengukur perilaku atau fungsi dari software
* Menggunakan analisis fungsi titik (function point analysis) untuk menilai kualitas software
* Menggunakan kompleksitas siklus (cyclomatic complexity) untuk menilai kompleksitas software

Selain itu, software testing juga dapat digunakan untuk mengevaluasi kualitas software dengan cara:

* Melakukan tes berdasarkan metrik yang paling rentan terhadap kesalahan
* Menggunakan model prediksi kecacatan (software fault prediction) untuk memprediksi kemungkinan kecacatan pada klas-klas tertentu

Dengan demikian, software quality dapat dinilai menggunakan kombinasi dari software metrics dan software testing.

### reference


---

## Sample 5

- conversation_id: 12
- user_chat_id: 449
- bot_chat_id: 450

### user_input

Apa itu machine learning?

### retrieved_context

1. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

3. TABLE 1. Classification by articles.

Dalam penelitian ini, terdapat beberapa jenis teknik pembelajaran mesin (machine learning) yang digunakan dalam siklus hidup perangkat lunak. Berdasarkan analisis artikel-artikel yang dipilih, dapat dilihat bahwa sekitar 73% dari total artikel (193/263) menggunakan teknik supervised learning untuk mendeteksi kelemahan atau kesalahan dalam kode program.

Dalam supervised learning, model dibuat dengan melibatkan dataset yang telah terlabel. Model ini kemudian digunakan untuk mengklasifikasikan data baru menjadi kategori "Buggy" (kesalahan) atau "Correct" (benar). Sementara itu, sekitar 6% dari artikel-artikel tersebut menggunakan teknik unsupervised learning, di mana model dibuat tanpa melibatkan dataset yang telah terlabel.

Selain itu, juga ditemukan bahwa sekitar 2% dari total artikel (4/263) menggunakan teknik semi-supervised learning dan sekitar 0.4% menggunakan reinforcement learning, serta 17% menggunakan analytical learning. Pada umumnya, metode klasifikasi yang paling banyak digunakan adalah ANN (Artificial Neural Network), diikuti oleh RF (Random Forest), DT (Decision Tree), dan NB (Naïve Bayes).

Dari data ini dapat disimpulkan bahwa artikel-artikel tersebut berfokus pada penggunaan teknik pembelajaran mesin untuk mendeteksi kelemahan dalam kode program, serta perbandingan antara berbagai metode klasifikasi. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8)

4. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

5. AI-based machine learning requires a huge number of inputs as the knowledge and different intelligent algorithms in order to make the right decision. By looking at an example using technology in unmanned vehicles, there will be a basic understanding of how machine learning or machine intelligence work. The development of machine intelligence is still far from mimicking the cognitive competence of the human brain. It is still challenging to deal with those data effectively and making a driving decision accurately and quickly [17]. Machine learning sometimes returns an inaccurate prediction based on the collection of training data and an engineer needs to make some adjustments to avoid significant losses in terms of public safety. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

6. TABLE 2. Electronic database.

Dalam penelitian ini, ditemukan beberapa pola penting dalam penggunaan teknik kecerdasan buatan (Artificial Intelligence) di bidang rekayasa perangkat lunak. Analisis yang dilakukan menunjukkan bahwa pembelajaran mesin (Machine Learning) adalah teknik AI yang paling umum digunakan.

Data menunjukkan bahwa ML telah digunakan secara luas dalam berbagai fase pengembangan perangkat lunak, termasuk fase analitik desain dan data persiapan. Hal ini menunjukkan bahwa ML dapat membantu mendukung aktivitas-aktivitas yang kompleks dan menghabiskan sumber daya.

Dalam fase pengujian, juga ditemukan bahwa ML digunakan secara luas untuk melakukan automasi tes perangkat lunak, sehingga membantu meningkatkan efisiensi dalam pengembangan perangkat lunak. Pada fase analitik desain dan data persiapan, ML juga menunjukkan kemampuan yang baik dalam mendukung aktivitas-aktivitas.

Dari analisis ini dapat disimpulkan bahwa AI telah menjadi bagian penting dalam rekayasa perangkat lunak modern. Penggunaan AI, terutama pembelajaran mesin, telah meningkatkan efisiensi dan produktivitas dalam pengembangan perangkat lunak. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 5)

7. By the type of ML, we mean how the models have been trained, i.e., supervised, semi-supervised, unsupervised, reinforcement, or analytical learning. Supervised learning is based on a training set and a test set taken from the dataset. The model training is done by taking multiple labeled samples from the train set. After the model is trained, its performance is evaluated using the test set. In semi-supervised learning, both labeled and unlabelled data are employed in order to train the model. The dataset is divided into unsupervised clusters as such. Then, the class information is obtained by learning the clustering outcomes [216]. Unsupervised learning requires no training dataset. For instance, in unsupervised learning for fault detection, software instances are usually grouped into clusters and each cluster is labeled as ''Buggy'' or ''Correct''. However, each cluster needs to be labeled manually by the individuals with expertise [198]. Reinforcement learning refers to unsupervised goal-oriented learning performed by an agent directly interacting with the environment. Analytical learning is aimed at generating solutions based on background knowledge and improving inference iteratively [253]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8)

8. TABLE 13. Results: ML Algorithms on Case Studies (All Features).

Dalam analisis ini, kita melihat hasil dari beberapa algoritma pemodelan machine learning (ML) pada studi kasus yang berbeda dengan fitur lengkap. Terdapat delapan studi kasus yang dipilih untuk perbandingan, yaitu CS1, CS2, CS3, CS5, CS6, CS7, dan CS8. Model-model ML yang digunakan dalam analisis ini adalah Support Vector Regressor (SVR), Linear Regression, K-Nearest Neighbor (k-NN), XGBoost Regressor, dan Artificial Neural Network (ANN).

Dari hasil perbandingan, terlihat bahwa beberapa algoritma memberikan hasil yang lebih baik daripada yang lain. Misalnya, ANN dan SVR menghasilkan hasil yang paling baik dalam studi kasus CS1 dan CS7 masing-masing dengan PRED - ISBSG = 0.953 dan Case Studies = 0.03, serta MMR E - ISBSG = 1.28 dan Case Studies = 1.28.

Dalam analisis ini juga terlihat bahwa model yang lebih kompleks seperti ANN tidak selalu memberikan hasil yang lebih baik daripada model yang lebih sederhana. Misalnya, CS2 dengan satu aktor kompleks menghasilkan hasil yang kurang baik daripada CS3 dan CS4.

Dari analisis ini dapat disimpulkan bahwa pilihan algoritma ML sangat mempengaruhi akurasi hasil dalam perhitungan biaya efisiensi software. Dengan demikian, penelitian lebih lanjut diperlukan untuk menentukan kombinasi model yang optimal dan fitur-fitur yang relevan bagi setiap studi kasus. (Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy, page 22)

### response

Machine Learning adalah teknik yang digunakan dalam rekayasa perangkat lunak untuk mendeteksi kelemahan atau kesalahan dalam kode program, serta untuk melakukan automasi tes perangkat lunak. Machine learning menggunakan algoritma-algoritma seperti pembelajaran mesin (ML) untuk menganalisis data dan membuat prediksi.

Dalam konteks ini, machine learning digunakan untuk:

* Mendeteksi kelemahan atau kesalahan dalam kode program dengan menggunakan teknik supervised learning
* Melakukan automasi tes perangkat lunak dengan menggunakan teknik pembelajaran mesin (ML)
* Membantu meningkatkan efisiensi dalam pengembangan perangkat lunak dengan menggunakan teknik AI

Jadi, jawaban singkatnya adalah: Machine Learning adalah teknologi yang digunakan untuk mendeteksi kelemahan atau kesalahan dalam kode program dan melakukan automasi tes perangkat lunak.

### reference


---

## Sample 6

- conversation_id: 12
- user_chat_id: 451
- bot_chat_id: 452

### user_input

Bagaimana machine learning dapat digunakan dalam software engineering untuk meningkatkan kualitas perangkat lunak?

### retrieved_context

1. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

2. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

3. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

5. This section discusses the techniques used to identify opportunities to use refactoring techniques based on Machine Learning (ML) algorithms. Then, we discuss the various effects of refactoring techniques on software quality attributes. (Revisiting Scenarios of Using Refactoring Techniques to Improve Software Systems Quality, page 1)

6. TABLE 6. Application, improvement and development of artificial intelligence techniques in the primary studies. TABLE 6. Aplikasi, peningkatan, dan pengembangan teknik kecerdasan buatan dalam studi primer menunjukkan berbagai cara peneliti telah menggunakan teknik kecerdasan buatan dalam software engineering. Terdapat beberapa pola yang dapat dilihat dari data ini.

Kolom "Technique" menampilkan variasi teknik kecerdasan buatan, seperti Machine Learning (ML), Natural Language Processing (NLP), dan Hybrid ML. Keterlibatan ML sangat menonjol dalam studi-studi tersebut, baik secara individu maupun kombinasi dengan teknik lain.

Dari "Application", dapat dilihat bahwa peneliti telah menggunakan AI untuk berbagai tujuan, termasuk prediksi kegagalan software, klasifikasi permintaan pengguna, analisis data besar, dan lain-lain. Penekanan pada pengembangan model yang didorong oleh data tampaknya menjadi fokus utama banyak peneliti.

"Improvement and Development" menunjukkan bahwa AI tidak hanya digunakan untuk aplikasi tetapi juga untuk meningkatkan kemampuan beberapa teknik dalam software engineering, seperti perbaikan akurasi prediksi risiko keamanan dan pengembangan model yang lebih maju. Kegunaan dari kombinasi antara Machine Learning dengan Neural Network (ANN) tampaknya menjadi bidang penelitian penting.

Pada "Primary Studies", variasi jenis studi yang menggunakan AI dalam software engineering dapat dilihat, seperti penggunaan model data didorong untuk analisis sistem, penelitian pada kemampuan AI dalam memprediksi kegagalan, dan pengembangan model yang lebih akurat dengan bantuan dari teknik kombinasi ML.

Dalam keseluruhan, tabel ini menunjukkan bahwa peneliti telah mengembangkan berbagai aplikasi dan teknologi yang menggunakan kecerdasan buatan dalam software engineering. Penggunaan AI telah diterapkan untuk meningkatkan akurasi prediksi, memperbaiki kemampuan klasifikasi, serta pengembangan model yang lebih maju dengan bantuan dari kombinasi teknik-teknik yang berbeda-beda.

Penggunaan kecerdasan buatan secara luas dalam beberapa bidang termasuk software engineering menunjukkan bahwa teknologi ini memiliki potensi besar untuk meningkatkan kinerja, memperbaiki akurasi analisis data, dan mengembangkan model yang lebih akurat. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 9)

7. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

8. In order to facilitate requirements traceability, researchers have suggested that devising a feedback mechanism, such as adding user feedback during the model training process in order to improve feature selection and performance, can really help the cause of generalizability. One of such works is presented by Sultanov et al. [3], which provides a very good basis for further developments.

In order to improve prediction accuracy and better reliability of results, more experiments using larger numbers of datasets and software applications have also been suggested [99], [115], [188], [237].

Researchers in the articles have also suggested investigating further regarding the suitable metrics and loss functions employed in the evaluation of ML for SE-focused techniques, especially for multi-class classification problems [125].

Future research directions also include automata learning for emergent middle-wares and using ML to address complex system integration problems, especially in system of systems such as the internet of things. Moreover, researchers are encouraged to devise adaptable, easily integrable, and scalable solutions in the area. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 13)

### response

Machine learning dapat digunakan dalam beberapa cara untuk meningkatkan kualitas perangkat lunak:

• Membantu deteksi kerusakan pada kode dengan menggunakan algoritma seperti Support Vector Machines (SVM), Naive Bayes (NB), Decision Trees, dan Neural Networks.
• Menggunakan metrik pengukuran yang dapat membantu dalam menilai kinerja software dan mendeteksi potensi masalah sebelumnya ditemukan.
• Membantu dalam meningkatkan efisiensi testing dengan memprediksi bagian kode mana yang paling rentan terhadap kerusakan sehingga perlu diuji lebih lanjut.

Jadi, machine learning dapat digunakan untuk mendeteksi kerusakan pada kode, mengidentifikasi potensi masalah, dan meningkatkan efisiensi testing.

### reference


---

## Sample 7

- conversation_id: 12
- user_chat_id: 453
- bot_chat_id: 454

### user_input

Apa itu software development?

### retrieved_context

1. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

2. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

3. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. Software requirements outline the purpose of the development and design. It serves as the foundation of software intended to develop [1]. Requirements are defined in the beginning and act as a developmental milestones to accomplish successful executable software components [2]. Software requirement engineering is a systematic approach that is significantly developed in the course of the most recent decade [3]- [5]. Software architecture can be viewed as an organization of a system that comprehensively includes components interactions, operational environments, design principles, software functionalities, and often covers future evolutionary software perspective [6]- [9]. (Integration of Software Architecture in Requirements Elicitation for Rapid Software Development, page 1)

5. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

6. Software development is a set of activities which time, budget, and effort of the human resource. Over the years, the software development process has matured to enable the adaptation and integration of commercially available components. The availability of commercially-off-the-shelf and modifiable-off-the-shelf components has transferred the complexity from development and design phases to the integration phase and we can observe large-application development by integrating the available components. Often, due to the limitation of technological and other resources, developing a software application in-house may be less beneficial. In such circumstances, development firms opt to either buy software or outsource the development. In this paper, we identify the factors that govern the decision of making software applications in-house, outsourcing them, or buying them from the market. Since the concept of component integration is more common in large scale applications, in this paper we consider this case. INDEX TERMS Software make vs buy decision, software outsourcing, domestic outsourcing. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

7. Software development is a set of activities which time, budget, and effort of the human resource. Over the years, the software development process has matured to enable the adaptation and integration of commercially available components. The availability of commercially-off-the-shelf and modifiable-off-the-shelf components has transferred the complexity from development and design phases to the integration phase and we can observe large-application development by integrating the available components. Often, due to the limitation of technological and other resources, developing a software application in-house may be less beneficial. In such circumstances, development firms opt to either buy software or outsource the development. In this paper, we identify the factors that govern the decision of making software applications in-house, outsourcing them, or buying them from the market. Since the concept of component integration is more common in large scale applications, in this paper we consider this case. INDEX TERMS Software make vs buy decision, software outsourcing, domestic outsourcing. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

8. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

### response

Software development adalah aktivitas yang melibatkan serangkaian prosedur yang menghasilkan perangkat lunak sebagai keluaran.

### reference


---

## Sample 8

- conversation_id: 12
- user_chat_id: 455
- bot_chat_id: 456

### user_input

Bagaimana software development berhubungan dengan Agile software development dan software testing?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

6. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

7. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

8. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

### response

Agile development methodologies digunakan oleh perusahaan pengembangan software untuk meningkatkan efisiensi dan kualitas produk. Meskipun demikian, manajemen proyek Agile dapat menjadi tantangan, terutama dalam kasus kecil dan menengah (SMEs). Product Owner dan Scrum Master harus memastikan kualitas produk dan efektifitas tim serta proses.

Agile development tidak secara langsung berhubungan dengan software testing. Namun, beberapa sumber menyebutkan bahwa Agile digunakan dalam konteks software development yang melibatkan kegiatan tes (testing).

Agile development dihubungkan dengan software analytics tools untuk meningkatkan kualitas produk melalui feedback cycle yang singkat dan adaptasi terhadap perubahan pasar.

Perlu diperhatikan bahwa beberapa sumber tidak secara eksplisit menyebutkan hubungan antara Agile development, software testing, dan pengembangan software.

### reference


---

## Sample 9

- conversation_id: 12
- user_chat_id: 457
- bot_chat_id: 458

### user_input

Apa itu software maintenance?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

3. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

4. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

5. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

6. Variant management is another major area of modern vehicle development and production. It refers to the classification of which features in the vehicle should be standard and which ones should be offered in variants. The aim is always to keep the cost for variation low as well as address the different constraints and markets. Variant handling concepts already exist and are widely used in the automotive industry. OEMs basically develop and manage variants in software using variant coding. Software variants are a group of similar services or applications in terms of their provided features in the vehicles. Thus, we anticipate that this new software update scheme is useful to variability-rich development and deployment of software modules introduced to the vehicles in both the automotive engineering and cloud communities. In particular, configurations for the entire vehicle at all levels are derived based on different factors. Such factors include parameters of configurable third-party modules, parameters of the used hardware, and the selection of user data and subscriptions for the services. The next section will demonstrate how our scheme, combining a digital signature and a Merkle hash tree, achieves synergistic authentication and verification of multiple software variants. It allows OEMs to efficiently manage and control different software variants, while also maintaining the highest standards of security and reliability. (A Novel Variability-Rich Scheme for Software Updates of Automotive Systems, page 1)

7. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

8. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

### response

Software maintenance adalah fase di mana pengguna atau developer menemukan masalah dan memperbaikinya sebelum atau setelah rilis berikutnya, tergantung pada tingkat keparahan.

### reference


---

## Sample 10

- conversation_id: 12
- user_chat_id: 459
- bot_chat_id: 460

### user_input

Bagaimana software maintenance membantu menjaga software quality setelah proses software development selesai?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

3. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

4. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

5. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

6. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

7. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

8. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

### response

Melalui kegiatan pemeliharaan, para pengguna atau pengembang dapat menemukan masalah dan memperbaikinya sebelum rilis berikutnya, tergantung pada tingkat keseriusannya. Software maintenance juga membantu meningkatkan software quality dengan mengurangi biaya testing dan perawatan.

### reference


---

## Sample 11

- conversation_id: 12
- user_chat_id: 461
- bot_chat_id: 462

### user_input

Apa itu deep learning?

### retrieved_context

1. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Many kinds of research attempt to find solutions for the current obstacles of Machine Learning Systems. To draw optimal decision making, approaches such as Fault Tree Analysis, Fuzzy Logic, Metaheuristic Algorithm, and Artificial Neural Network are developed to test with a huge amount of training data by using different algorithms. However, the sufficiency and versatility of Deep Learning systems are based on the accuracy of the test data set. It is difficult to provide adequate support due to the accessibility of test data quality issue. The current Deep Learning systems have various vulnerabilities and their system analysis and defect detection are extremely difficult. Unlike traditional software systems, Machine Intelligence does not have a clear controllable logic and understandability since the process to make decisions rely on the training data. The recent study shows two major vulnerabilities in Deep Learning systems: Software quality from the output of Deep Learning alone is not adequate; and Failure in unseen attacks even though Deep Learning is immune to known types of attacks [18], [19]. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

3. Software Defects Prediction (SDP) consists in identifying defective software components, being considered an essential activity during software development. It represents the activity of identifying defective software modules in new versions of a software system [1]. SDP is considered of great importance in software engineering, as it contributes to continuously improving the software quality. Developing high quality software systems is expensive and, in this context, SDP is used for increasing the cost effectiveness of quality assurance and testing [2]. By detecting fault-prone modules in new versions of a software system, SDP helps to allocate the effort so as to test more thoroughly those modules [1]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

4. Table 12 presents, for each classiﬁer c ∈{ DL-FASTAI, Table 12 memaparkan hasil analisis dari beberapa jenis klasifikator dalam penggunaan prediksi kelemahan perangkat lunak berbasis deep learning. Dua variabel utama yang diperhatikan adalah "sensitivity" (Sens) dan "AUC" (Area Under Curve). Sensitivity merupakan ukuran yang menunjukkan kemampuan klasifikator dalam mendeteksi kasus kelemahan yang sebenarnya. Sementara itu, AUC merupakan indikasi performa yang lebih komprehensif, menunjukkan kemampuan klasifikator untuk membedakan antara kasus kelemahan dan non-kelemahan.

Dari data yang tersedia, tidak ada informasi yang cukup spesifik tentang nilai-nilai khusus dari Sens dan AUC untuk setiap klasifikator. Namun, perlu diingat bahwa hasil analisis ini mungkin membantu para peneliti memahami pola umum performa antara berbagai jenis klasifikator dalam konteks prediksi kelemahan perangkat lunak dengan menggunakan deep learning. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 14)

5. With the rapid development of information technology, the scale of data appears explosive growth. Mining valuable information from complex data has great practical significance [1]. As an important method in the field of data mining, clustering algorithm is widely used in data analysis and mining. DBSCAN algorithm is a typical clustering algorithm, and data density is as a measure, which can identify arbitrary shape classes and noise points of data sets. Some data show that by 2020, the data accumulated by China will account for 20% of the global data. Nowadays, both the government and enterprises have accumulated a large amount of data [2], and mining useful information from these data has great research value. As an important technology in the field of data mining, clustering has been applied in many fields, such as pattern recognition, information retrieval, network public opinion prediction and so on. (DBSCAN-Based Automatic De-Duplication for Software Quality Inspection Data, page 1)

6. Deep learning-based approaches show great potential to address power line inspection tasks. However, existing work still faces challenges with the complex backgrounds and real-time applications. Additionally, considering the timing and computational resource constraints, further exploration is necessary to develop a resource-efficient model that can be deployed on UAVs, ensuring efficient processing and reliable communication between the UAV and the ground station. The literature study highlights the necessity of developing a complete scheme that ensures connectivity, privacy, and security in the communication between the UAV and ground station, as well as developing a model that is accurate and light enough to mount to a UAV. (LCUT-Sv9: UAV-Assisted Powerline Inspection Framework with Secure Time-Sensitive Communication for Industry 5.0, page 4)

7. Apart from communication paradigms, DeepLabV3 and a modified U-Net were used to enhance efficiency and reliability with UAV imagery segmentation tasks, significantly improving the accuracy and robustness [9]. TLSUNet combined U-Net with a lightweight backbone structure and contextual information features to optimize segmentation tasks by reducing computational complexity while maintaining high accuracy [10]. A lightweight segmentation network was introduced for the real-time detection of broken strands on power lines, thus enhancing the efficiency of inspection processes [11]. Recent research combined attention mechanisms with a dual-branch approach to improve detection. It achieved high accuracy in segmenting power lines and towers using Light Detection and Ranging (LiDAR) data from UAVs, leveraging multiscale density features and pointbased deep learning techniques [12]. (LCUT-Sv9: UAV-Assisted Powerline Inspection Framework with Secure Time-Sensitive Communication for Industry 5.0, page 2)

8. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

### response

Deep Learning adalah desain yang dirancang untuk meneruskan analisis data dengan struktur logika seperti bagaimana seorang manusia dapat menarik kesimpulan. Deep Learning membutuhkan jumlah besar dataset untuk menggunakan input dalam algoritma untuk menghasilkan prediksi yang lebih akurat.

### reference


---

## Sample 12

- conversation_id: 12
- user_chat_id: 463
- bot_chat_id: 464

### user_input

Bagaimana deep learning berbeda dari machine learning dan bagaimana manfaatnya untuk pengembangan sistem AI?

### retrieved_context

1. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Many kinds of research attempt to find solutions for the current obstacles of Machine Learning Systems. To draw optimal decision making, approaches such as Fault Tree Analysis, Fuzzy Logic, Metaheuristic Algorithm, and Artificial Neural Network are developed to test with a huge amount of training data by using different algorithms. However, the sufficiency and versatility of Deep Learning systems are based on the accuracy of the test data set. It is difficult to provide adequate support due to the accessibility of test data quality issue. The current Deep Learning systems have various vulnerabilities and their system analysis and defect detection are extremely difficult. Unlike traditional software systems, Machine Intelligence does not have a clear controllable logic and understandability since the process to make decisions rely on the training data. The recent study shows two major vulnerabilities in Deep Learning systems: Software quality from the output of Deep Learning alone is not adequate; and Failure in unseen attacks even though Deep Learning is immune to known types of attacks [18], [19]. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

3. AI-based machine learning requires a huge number of inputs as the knowledge and different intelligent algorithms in order to make the right decision. By looking at an example using technology in unmanned vehicles, there will be a basic understanding of how machine learning or machine intelligence work. The development of machine intelligence is still far from mimicking the cognitive competence of the human brain. It is still challenging to deal with those data effectively and making a driving decision accurately and quickly [17]. Machine learning sometimes returns an inaccurate prediction based on the collection of training data and an engineer needs to make some adjustments to avoid significant losses in terms of public safety. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

4. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

5. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

6. The associate editor coordinating the review of this manuscript and approving it for publication was Diego Oliva . aim to increase the likelihood of finding vulnerabilities and reduce the time required for software engineers to discover these vulnerabilities. SE phases involve various activities that range across all the stages of the Software Development Lifecycle (SDLC) phases. AI techniques like machine learning (ML), heuristic algorithms (HA), deep learning (DL), data mining (DM), data analytics (DA), and natural language processing (NLP) have been widely explored in the SE phases. As software grows in size, its complexity increases, along with the time and cost required for its overall construction. Extensive data is generated from all the SDLC stages. This data varies between the planning, requirements engineering, design, system development, testing, deployment, training, and maintenance phases [2]. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

7. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

8. AI-based video software systems integrate artificial intelligence (e.g., machine learning and deep learning models) to process and analyze video data for tasks like object detection, event recognition, video synthesis, and analytics. With the proliferation of deep learning techniques, the capabilities and complexity of video processing applications have expanded significantly. This rapid growth in AI-driven video applications, exemplified by modern generative video platforms like OpenAI's Sora [1] and OpusClip [2], has elevated the importance of software architecture and quality attributes in ensuring these systems are robust and maintainable. Designing effective architecture is critical because the interplay between architectural style and desired quality attributes (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

### response

Deep Learning memiliki perbedaan mendasar dengan Machine Learning, yaitu:

• **Struktur Logika**: Deep Learning dirancang untuk terus menganalisis data dengan struktur logika yang meniru cara manusia mengambil kesimpulan.
• **Penggunaan Data Besar**: Deep Learning memerlukan jumlah data besar sebagai input dalam algoritma untuk mendapatkan prediksi yang lebih akurat.

Manfaat dari Deep Learning adalah:

• **Penyempurnaan Prediksi**: Dengan penggunaan data besar, Deep Learning dapat meningkatkan akurasi prediksi.
• **Pengembangan Sistem AI yang Lebih Baik**: Deep Learning membantu mengembangkan sistem AI yang lebih baik dengan meniru cara manusia berpikir.

Namun, perlu diingat bahwa manfaat Deep Learning juga dipengaruhi oleh kualitas data yang digunakan.

### reference


---

## Sample 13

- conversation_id: 12
- user_chat_id: 465
- bot_chat_id: 466

### user_input

Apa itu software metrics?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

4. TABLE 2. Class-level software metric used in this study.

Tabel ini memuat beberapa metrik kelas untuk prediksi kesalahan perangkat lunak. Data tabel menunjukkan bahwa ada dua dataset utama: Software Metrics dan Full Dataset. Kedua dataset tersebut berbeda dalam hal variabel independen yang digunakan, yaitu ESM (Error-Severity Metric) values dan software metrics yang diekstraksi dari modul perangkat lunak.

Pada tabel ini, kita dapat melihat bahwa terdapat tiga jenis metrik ESM: IndexOutOfBounds, NullPointer, dan ClassCast. Masing-masing metrik tersebut memiliki nilai-nilai yang berbeda-beda pada kedua dataset. Pada Software Metrics Dataset, variabel independen hanya mencakup software metrics, sedangkan pada Full Dataset juga termasuk ESM values.

Dengan memperhatikan tabel ini, kita dapat menyimpulkan bahwa peneliti menggunakan metrik-metrik tersebut untuk memprediksi kesalahan perangkat lunak. Pada dataset yang lebih lengkap (Full Dataset), penulis juga melibatkan ESM values sebagai variabel independen tambahan. Hal ini menunjukkan bahwa penulis ingin mengetahui bagaimana pengaruh nilai-nilai ESM terhadap performa model pelatihan machine learning.

Dalam konteks yang lebih luas, tabel ini memberikan gambaran tentang cara peneliti menggunakan metrik kelas untuk prediksi kesalahan perangkat lunak. Penemuan penulis dapat berguna dalam meningkatkan akurasi model pemodelan perangkat lunak dan mengidentifikasi potensi masalah yang mungkin terjadi pada sistem. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 6)

5. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

6. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. In the SLR, we generalized metrics collection methods among six categories. The collected metrics are a key input for evaluation, prediction, characterization, and improvement of software development process. In this survey, majority of the organizations only collect most common FIGURE 16. Frequency of metrics collection methods in software organizations.

metrics (23%) or necessary metrics (30%) for software process improvement. The SMEs (20%), large (22%) and very large (37%) organizations collect metrics that are necessary for software process improvement. The most common metrics are collected by SMEs (30%), large (30%) and very large (11%) organizations as shown in Figure 16. The use of measurement tools and expert judgment is used by 14% of organizations. The use of automated tools, measurement models and expert judgment is under 15% among the organizations. The use of measurement models is least used method for metrics collection while on the other hand, there are 35 measurement models proposed in literature. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 11)

8. There is a long history of research on metrics programs (MPs) [24], and plenty of literature recommending success factors for their implementation [17], [28], [34], [44]. However, literature on SMEs using MPs in the context of Agile is rather scarce. Moreover, the literature on measuring software processes and their role in improving SME processes is even scarcer. Measuring software processes with the use of process metrics enables objective and quantitative evaluation of software processes, which can lead to continuous improvement and learning [34], [42]. However, measuring process metrics is a challenge [43]. Software processes are inherently complex and intangible, which makes their measurement more difficult than their product counterparts [19], [41]. Ideally, measurement activities should consume little effort and time, while being adequate enough to meet an organization's measurement demands. Software organizations need to weigh in cost-efficiency while prioritizing measurement objectives and targets. SMEs have the added constraints of limited budget, ambitious deadlines, and short-term strategy [45]. Due to these reasons, measuring software processes, especially in an SME, becomes a bigger challenge. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

### response

Software metrics adalah ukuran-ukuran yang digunakan untuk mengukur kualitas dan kompleksitas perangkat lunak. Contoh software metrics antara lain function point analysis, cyclomatic complexity metric, ESM (Error-Severity Metric) values, dll.

### reference


---

## Sample 14

- conversation_id: 12
- user_chat_id: 467
- bot_chat_id: 468

### user_input

Bagaimana software metrics dapat digunakan untuk mengevaluasi software quality dan software maintenance?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

4. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

5. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

6. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

7. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

8. The metrics of object-oriented are utilized for prediction of software quality. The characteristics that ascertain the software quality are understandability, fault tolerance, maintainability, defect density, reusability, normalized rework rate, and many others. Numerous studies have been performed including object-oriented metrics verification through empirical research paper on open-source software in the context of fault prediction utilizing {loc}, {lcom}, {cbo}, {dit}, and {noc} metrics [80]. Reusability investigation on systems based on object-oriented utilizing metrics of coupling, inheritance, and cohesion [81], heuristic-based C&K metrics evaluation [82], reusability metrics for the design of objectoriented [83], empirical scrutiny of C&K metrics for the complexity of object-oriented design [84]. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 12)

### response

Software metrics dapat digunakan untuk mengevaluasi software quality dengan cara:

* Membantu pengembang software dalam memantau kualitas software secara berkala
* Mengukur kompleksitas software dan mengidentifikasi potensi kesalahan
* Menganalisis efisiensi dan keamanan sistem software

Selain itu, software metrics juga dapat digunakan untuk mengevaluasi software maintenance dengan cara:

* Mengukur perubahan kode yang dilakukan selama proses pemeliharaan
* Mengidentifikasi lokasi yang paling rentan terhadap kesalahan
* Menganalisis kemampuan sistem dalam mendukung perubahan dan perkembangan.

### reference


---

## Sample 15

- conversation_id: 12
- user_chat_id: 469
- bot_chat_id: 470

### user_input

Apa itu software testing?

### retrieved_context

1. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Testing is a comprehensive concept related to the development of each system. In the software engineering discipline, testing is a crucial task of the software development life cycle. In contrast, software testing in any field other than software engineering can be considered as an end-user testing focused on the suitability of a software developed for a specific purpose in this field. For this reason, the multidisciplinary use of software testing makes it difficult to create a specific corpus of software testing studies in the scope of software engineering. In this context, to create a specific corpus of software testing within the scope of software engineering, a methodology including two sequential stages was followed for corpus creation, which included identifying core publication sources for the software engineering field and extracting articles specific to software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

5. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

7. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

8. The testing phase of the SDLC aims to make sure that all the system components provide their required functionality alone and as part of the whole system. Software testing is the most time-consuming, complicated, and costly process of the SDLC [92]. This phase is an important component of improving the efficiency of software development projects [32]. While it is an essential part of software development, rigorous testing is not always a focus of software engineering education [93]. As a result of this shortcoming, software developers often regard software testing as a liability, lowering overall software quality. Threat modeling is a systematic method for identifying threats that may compromise security, and it is considered a well-known accepted practice by the software testing industry [94]. This phase aims to find possible bugs and errors in the system and remove them. The present study identified 64 papers to discuss software security risks during software testing phase of SDLC. Some common security risks involved in this phase are as follows [5], [22], [95]- [98]: (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 11)

### response

Software testing adalah "aktivitas di mana suatu sistem dieksekusi di bawah kondisi yang spesifik, hasilnya diamati atau direkam, dan evaluasi dilakukan terhadap aspek tertentu dari sistem" (ISO/IEC 24765, 2006) [6].

### reference


---

## Sample 16

- conversation_id: 12
- user_chat_id: 471
- bot_chat_id: 472

### user_input

Bagaimana software testing membantu menemukan masalah dan meningkatkan software quality?

### retrieved_context

1. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

2. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

4. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

5. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. Software Defects Prediction (SDP) consists in identifying defective software components, being considered an essential activity during software development. It represents the activity of identifying defective software modules in new versions of a software system [1]. SDP is considered of great importance in software engineering, as it contributes to continuously improving the software quality. Developing high quality software systems is expensive and, in this context, SDP is used for increasing the cost effectiveness of quality assurance and testing [2]. By detecting fault-prone modules in new versions of a software system, SDP helps to allocate the effort so as to test more thoroughly those modules [1]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

7. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

8. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

### response

Software testing membantu menemukan masalah dan meningkatkan software quality dengan:

* Mengevaluasi perilaku sistem perangkat lunak untuk memastikan bahwa itu sesuai dengan spesifikasinya (ISO/IEC 24765, 2006) [6]
* Mengidentifikasi klas yang paling rentan terhadap kesalahan dan mengoptimalkan alokasi sumber daya tes (Sumber: Experimental Validation of Inheritance Metrics' Impact on Software Fault Prediction)
* Meningkatkan efektivitas tes dengan menggunakan metrik software untuk meningkatkan efektifitas tes (Sumber: Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper)

### reference


---

## Sample 17

- conversation_id: 12
- user_chat_id: 473
- bot_chat_id: 474

### user_input

Apa itu systematic literature review?

### retrieved_context

1. Table 1. Researchers have used the SLR process in several domain sebagai dasar penelitian ini membagikan beberapa metode dan langkah dalam melakukan Systematic Literature Review (SLR). Secara singkat, SLR adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan.

Dalam fase perencanaan, para peneliti harus menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan. Mereka juga harus menetapkan kriteria inklusi dan eksklusi untuk memilih artikel-artikel yang akan diintervensi.

Fase pelaksanaan melibatkan proses mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya. Para peneliti harus mengidentifikasi informasi yang relevan, mengumpulkan data, serta melakukan analisis untuk mendapatkan hasil yang diinginkan.

Fase tinjauan adalah tahap akhir dalam proses SLR. Pada fase ini, para peneliti akan meninjau dan menganalisis hasil-hasil dari fase sebelumnya. Mereka juga harus memastikan bahwa hasil penelitian mereka tidak memiliki bias atau kesalahan.

Dalam beberapa domain yang telah diidentifikasi oleh peneliti, metode SLR digunakan untuk mengurangi ketidakakuratan dan kesalahan dalam penelitian. Penulis juga menggunakan teknik inter-rater reliability analisis untuk memastikan bahwa hasil-hasil dari fase tinjauan tidak memiliki bias.

Dalam beberapa kasus, metode SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

2. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

3. FIGURE 1. Steps of the systematic literature review process.

Gambar ini merupakan sebuah diagram alur proses sistematis tinjauan literatur, dengan menggunakan jenis visual yang disebut flowchart. Elemen yang tampak dalam gambar tersebut adalah serangkaian simbol dan garis yang membentuk alur proses. Terdapat beberapa elemen kunci yang dapat dilihat, yaitu:

* Simbol "1." pada bagian atas gambar yang menunjukkan tahap awal dari sistematis tinjauan literatur.
* Garis horizontal yang menghubungkan simbol "1." dengan simbol berikutnya, menunjukkan bahwa tahap tersebut adalah langkah awal dalam proses sistematis tinjauan literatur.
* Simbol lainnya seperti lingkaran dan persegi panjang yang menggambarkan tahapan-tahapan selanjutnya dalam proses tersebut.

Meskipun tidak terdapat angka atau label penting secara eksplisit, namun dapat disimpulkan bahwa gambar ini menunjukkan bahwa sistematis tinjauan literatur dilakukan melalui beberapa tahap yang jelas dan sistematik. Maka dari itu, makna singkat yang dapat ditarik adalah bahwa proses sistematis tinjauan literatur merupakan suatu proses yang terstruktur dengan baik untuk mencari dan menganalisis informasi yang relevan. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

4. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

5. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

6. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

7. The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

The SLR technique was used to search for the most relevant literature by applying explicit inclusion and exclusion criteria for primary studies [38].

We followed the guidelines provided by Rockart [38] to conduct our SLR study. The approach consists of three main phases: planning, conducting, and reporting the review. A thorough discussion of the SLR study conducted for this research project can be found in our previously published articles [25], [63], [64]. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 3)

8. In this systematic literature review (SLR), we focused on examining the most reputable and reliable databases available to researchers, as previously mentioned. It is important to note that we allocated publications to specific databases based on the chronological order of the searches conducted, even though some papers might be present across multiple databases. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 5)

### response

Systematic Literature Review (SLR) adalah metode penelitian yang kompleks, melibatkan tiga fase utama: perencanaan, pelaksanaan, dan tinjauan. SLR adalah jenis studi sekunder di mana studi primer dipelajari secara tidak berpihak dan berulang-ulang untuk mendefinisikan, menerjemahkan, dan membahas bukti yang relevan dengan pertanyaan penelitian.

SLR memiliki beberapa fase, yaitu:
- Fase perencanaan: menentukan topik atau pertanyaan penelitian, serta mengidentifikasi sumber-sumber informasi yang relevan.
- Fase pelaksanaan: mencari dan menganalisis artikel-artikel yang telah dipilih berdasarkan kriteria sebelumnya.
- Fase tinjauan: meninjau dan menganalisis hasil-hasil dari fase sebelumnya.

SLR digunakan dalam beberapa domain, seperti informasi keamanan (security), pengembangan perangkat lunak (software development) dan sebagainya.

### reference


---

## Sample 18

- conversation_id: 12
- user_chat_id: 475
- bot_chat_id: 476

### user_input

Bagaimana systematic literature review membantu peneliti membandingkan metode machine learning dan deep learning?

### retrieved_context

1. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

2. In order to search for relevant literature, following the guidelines proposed by Petersen et al. [19], we devised a query that uses a two-element PICO search. Problem 'P': (requirement, specification, design, model, analysis, architecture, implementation, code, test, verification, validation, maintenance), and Intervention 'I': (machine learning, deep learning).

We have not considered Comparison 'C' and Outcome 'O' as this is out of the scope of this study. Following is the resultant query that was eventually used in all digital libraries: 1 (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

3. The conclusion of the study is manifold. We have provided an overview of the state-of-the-art in the area of machine learning for software engineering by evaluating carefully selected studies. We also proposed a classification scheme that highlights the overall applications of machine learning for software engineering in terms of SDLC stages. The classification shows the primary focus of researchers towards specific stages. This observation is one of the major contributions of this study. This study also reveals that the quality of primary studies in the domain of ML and SE is evidence-based with respect to the techniques being empirically evaluated by the researchers. We have also shown the relationship of SDLC stages with ML types, tools, and techniques. Although this research area is showing moderate growth in terms of the number of publications, further primary studies need to be conducted to emphasize other lesser explored SDLC stages such as maintenance. The challenges, limitations and future directions reported in this article should motivate and further guide researchers in the future. We believe this study provides the necessary impetus and further motivation to explore those SDLC stages, which have been given lesser attention to date with respect to the application of ML. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 18)

4. A comprehensive literature review is imperative to identify and analyze recent advances and contributions to GAI in SD. To facilitate a systematic and rigorous examination, it is essential to implement well-defined review protocols and structured methodologies. These protocols and methodologies must be employed to ensure the efficient organization, synthesis, and interpretation of the collected evidence.

The methodology adopted for this systematic literature review followed a modified version of the guidelines for systematic literature reviews in software engineering proposed by Kitchenham and Charters [45]. This approach has been extensively applied in the field of software engineering research, including software testing [46], software quality assessment [47], software defect prediction using artificial intelligence [40], application of AI in software design [41], [48], and more recently, GAI in software design [11].

The review process consists of a sequence of structured stages, as illustrated in Fig. 1, and is aligned with the PRISMA workflow, shown in Fig. 2  [49]. The methodology comprises three main phases: planning, execution, and reporting. During the planning phase, the review scope was defined, including the study period, research questions, inclusion and exclusion criteria, and the search strategy. In the execution phase, the previously defined protocol was applied to identify, screen, and select primary studies that addressed the research

TABLE 1. SD dimension in the GAI.

questions. The selected studies were systematically analyzed and synthesized during the final phase of the study.

The results of the review included statistical analyses of the publication trends, journal distributions, and quartile rankings. These findings were examined in detail to address the research questions formulated during the planning phase and provide a comprehensive understanding of the current state of research on GAI in the SDLC.

To identify GAI opportunities for SD, it is necessary to examine the following research questions, which correspond to the four aspects of this study. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 4)

5. A comprehensive literature review is imperative to identify and analyze recent advances and contributions to GAI in SD. To facilitate a systematic and rigorous examination, it is essential to implement well-defined review protocols and structured methodologies. These protocols and methodologies must be employed to ensure the efficient organization, synthesis, and interpretation of the collected evidence.

The methodology adopted for this systematic literature review followed a modified version of the guidelines for systematic literature reviews in software engineering proposed by Kitchenham and Charters [45]. This approach has been extensively applied in the field of software engineering research, including software testing [46], software quality assessment [47], software defect prediction using artificial intelligence [40], application of AI in software design [41], [48], and more recently, GAI in software design [11].

The review process consists of a sequence of structured stages, as illustrated in Fig. 1, and is aligned with the PRISMA workflow, shown in Fig. 2  [49]. The methodology comprises three main phases: planning, execution, and reporting. During the planning phase, the review scope was defined, including the study period, research questions, inclusion and exclusion criteria, and the search strategy. In the execution phase, the previously defined protocol was applied to identify, screen, and select primary studies that addressed the research

TABLE 1. SD dimension in the GAI.

questions. The selected studies were systematically analyzed and synthesized during the final phase of the study.

The results of the review included statistical analyses of the publication trends, journal distributions, and quartile rankings. These findings were examined in detail to address the research questions formulated during the planning phase and provide a comprehensive understanding of the current state of research on GAI in the SDLC.

To identify GAI opportunities for SD, it is necessary to examine the following research questions, which correspond to the four aspects of this study. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 4)

6. There are two different techniques to identify the primary sources for literature review studies [44]. In the first technique, which is common in the software engineering community, search strings are developed and then executed on different digital libraries (e.g., ACM Digital Library) [45].

The second one is more common in the information systems community and starts with identifying a pool of initial papers, followed by the backward snowballing technique [23]. Jalali and Wohlin [44] applied both techniques on Agile practices in Global Software Engineering (GSD) and realized that although these techniques led to the identification of different sets of studies, no significant differences were observed in the findings. Human values have been researched in many domains across different research areas. In Section II, we discussed that there is no consensus on what human values are, and there are many values models that cover a different number of human values with various terminologies. Further to this, there is no established theory on human values within the software engineering community [19]. Due to these limitations, it was not possible for us to build a search string that covers all human values and execute it on different digital libraries. Hence, we decided to follow the approach proposed by Webster and Watson in the information systems community, which includes the following two steps [23]. Figure 2 shows our paper collection process. (Operationalizing Human Values in Software Engineering: A Survey, page 6)

7. In the future, we intend to perform a more comprehensive study investigating the relationship between ML and SDLC stages. To this end, we intend to narrow down our search query by including ML terms such as classification, regression, SVM, ANN, inductive logic, Bayesian network, or deep belief network. We believe in this way, we can grasp a more focused view of the state-of-the-art. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 18)

8. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

### response

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 19

- conversation_id: 12
- user_chat_id: 477
- bot_chat_id: 478

### user_input

Apa itu Agile software development?

### retrieved_context

1. As a result of this session, the metrics that were considered more valuable are (see Table 2):

• Metric #7: Estimation accuracy per development tasks (per developer in project in specific timespan).

• Metric #9: Number of development tasks with lacking estimation of effort to be spent (''estimated'') per project per developer.

• Metric #10: Number of development tasks with lacking value of effort used (''spend'') per project per developer.

• Metric #11: Total sum of estimated effort values (''estimate'') per project per developer.

• Metric #12: Sum of used effort (''spend'') per project per developer.

• Metric #18: Number of development tasks with reported bug.

• Metric #19: Average time of task correction based on project board.

• Metric #20: Average time-to-correct of task based on the project board.  • Metric #21: Percentage of 'non-bug' type tasks to total tasks on the board.

These metrics significantly improve management of such processes as task estimation and bug fixing, which are crucial in rapid software development of high quality and stable software. Moreover, after applying those metrics, team management is now more efficient and transparent. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 9)

2. Standardization would accelerate progress by facilitating direct comparison of approaches, promoting code reuse, and establishing best practices for agent development. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 16)

3. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

4. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

5. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

6. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

7. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

8. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

### response

Agile software development adalah metodologi pengembangan perangkat lunak yang fleksibel dan mendukung kerja sama tim. Ini digunakan oleh banyak pengembang karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks.

(Sumber: Gambar 6 dari "An Evaluation of Software Measurement Processes in Pakistani Software Industry")

### reference


---

## Sample 20

- conversation_id: 12
- user_chat_id: 479
- bot_chat_id: 480

### user_input

Bagaimana Agile software development mempengaruhi software development, software testing, dan software maintenance?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

3. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

4. There is a long history of research on metrics programs (MPs) [24], and plenty of literature recommending success factors for their implementation [17], [28], [34], [44]. However, literature on SMEs using MPs in the context of Agile is rather scarce. Moreover, the literature on measuring software processes and their role in improving SME processes is even scarcer. Measuring software processes with the use of process metrics enables objective and quantitative evaluation of software processes, which can lead to continuous improvement and learning [34], [42]. However, measuring process metrics is a challenge [43]. Software processes are inherently complex and intangible, which makes their measurement more difficult than their product counterparts [19], [41]. Ideally, measurement activities should consume little effort and time, while being adequate enough to meet an organization's measurement demands. Software organizations need to weigh in cost-efficiency while prioritizing measurement objectives and targets. SMEs have the added constraints of limited budget, ambitious deadlines, and short-term strategy [45]. Due to these reasons, measuring software processes, especially in an SME, becomes a bigger challenge. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

5. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

6. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

7. Worldwide software development expenditure, for year 2014, was 3.8 billion dollars which included 23% quality control and testing cost for business applications [4]. Early fault detection helps save costs, time, and reduce the complexity of the software because it is proportionate to the testing. It is a well known fact that extensive testing are impossible [5]. Testing cost sometimes amounts to over fifty percent of the The associate editor coordinating the review of this manuscript and approving it for publication was Claudio Agostino Ardagna . entire software development cost. It is for these reasons that it is more feasible to detect and test classes with faults to produce software with better quality. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

8. Generally, many of the traditional SRGMs are based on similar assumptions [1], [8]. In some cases, faults detected during testing may not be corrected immediately. This delay in fault correction can be caused by various factors such as prioritization of tasks, availability of resources, or complexity of the fault. As a result, the software reliability growth process can be impacted, and traditional SRGMs may not accurately reflect the actual reliability of the software. To address this, some SRGMs have been developed to account for delayed fault correction and other factors that may affect the software reliability growth process [11], [12], [15]. Raymond and O'Reilly [6] noticed that beta testing plays a crucial role in the testing of OSS. Therefore, the test team for OSS is often separate from the development team. When a fault is detected in OSS, developers typically require additional time to communicate with testers and rectify the issue. This situation often leads to longer debugging times for OSS, and delays in the fault correction process are more likely to occur. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

### response

Berikut adalah jawaban berdasarkan konteks:

Agile software development memiliki beberapa dampak pada software development, software testing, dan software maintenance.

* Agile mempengaruhi software development dengan:
 + Menggunakan praktek-praktek agile seperti continuous integration untuk mendeteksi dan memperbaiki kesalahan secepat mungkin.
 + Meningkatkan fleksibilitas dan adaptasi terhadap perubahan pasar dengan menggunakan siklus umpan balik yang singkat.
* Agile mempengaruhi software testing dengan:
 + Meningkatkan kemampuan untuk mendeteksi dan memperbaiki kesalahan secepat mungkin melalui continuous integration.
 + Menggunakan praktek-praktek agile seperti continuous testing untuk meningkatkan efisiensi testing.
* Agile mempengaruhi software maintenance dengan:
 + Meningkatkan kemampuan untuk mendeteksi dan memperbaiki kesalahan secepat mungkin melalui continuous integration dan continuous testing.
 + Menggunakan praktek-praktek agile seperti continuous delivery untuk meningkatkan efisiensi dalam merilis perubahan software.

Informasi tersebut ditemukan pada beberapa sumber yang berbeda, yaitu [Source: Measuring and Improving Agile Processes in a Small-Size Software Development Company] dan [Source: Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study].

### reference


---

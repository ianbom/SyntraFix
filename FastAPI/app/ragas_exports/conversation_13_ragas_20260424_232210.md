# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 1

- conversation_id: 13
- user_chat_id: 481
- bot_chat_id: 482

### user_input

Apa itu software engineering?

### retrieved_context

1. From SWEBOK ISO/IEC TR 1975:2015, we adopt the critical knowledge areas in software engineering to use as synonyms for software engineering. Twelve knowledge areas identified from the keywords were selected as most prevalent in the literature. These include software requirements, software design, software construction, software maintenance, software testing, software configuration management, software management, software process, software models and methods, and software quality. This is seen in similar SMSs in software engineering by other researchers Klotins et al. [40]. These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

2. Since the formulation of the term Search-Based Software Engineering (SBSE) [1], SBSE has attracted many research theories and applications. SBSE converts a software engineering problem into a computational search problem. The technique is based on the definition of the pool of possible solutions, which is known as the search space. Taking into account the complexity of modern software systems, the search space is too large to be explored exhaustively. To find a sufficiently good solution, SBSE follows the procedure that allows the selection of a potential solution from the search space based on given criteria. SBSE techniques (SBSET) have been applied at almost all the phases of the software development process starting from the requirement analysis [2], following software design, development, and refactoring [3], debugging and (The Acceptance of Search-Based Software Engineering Techniques: An Empirical Evaluation Using the Technology Acceptance Model, page 1)

3. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. Software engineering is a discipline that is concerned with various phases of software production from the preliminary requirement gathering stage through to maintenance of the software system. It is therefore concluded that software engineering is a discipline that leads to a systematic approach where cost effective software development is performed. Regardless of the speedy progress, the software industry is well thought-out by several to be in a crisis. At that time the average software projects exceed the schedule by half. Similarly, large number of projects were either not functioning as expected or were not used at all. There are numerous other challenges, industry needs to deal with, if it continued to step forward for much more mature engineering discipline. Varying situational contexts among team members are one of the many challenges that can lead to failure software if left unattended. Software engineering standards significantly acknowledge the importance of situational contexts. In this study we have investigated the IEEE standards association for the relevant standards. We found 32 most relevant stanafter performing filtration on the data set. We concluded that these software engineering standards significantly acknowledge towards consideration of situational contexts for successful software. Each standard is investigated for the various factors and sub-factors that can lead to varying situational contexts among software engineering team members. Based upon the analysis, we came across a pattern in the identified standards. We reported 8 categories under which these standards are grouped. Each of the standard reports the factors and sub-factors related to its category. The identified factors are 12 in number. Each of them is further grouped with the related sub-factors (52 in number) that ultimately can lead to failure software if not addressed properly. This study provides a guideline for the practitioners to consider these factors and sub-factors while performing software development in order to have a successful software development. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 11)

5. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

6. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

7. In pursuance of the issues raised from the empirical literature, it is necessary for process theory to transform software engineering body of knowledge especially paying attention to SSCs. Additionally, research in software engineering has been predominately prescriptive and method-focused [39], producing thousands of software development methods that remain underutilized. In order to solve the challenges with software practice, practitioners and researchers should contribute to the body of knowledge [135], given that SSCs dominate the industry and are responsible for over 80% of software produced in the market. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

8. A close look at the knowledge areas of software engineering used by the companies as reported in the selected articles indicates that general software development and project management are most prominent in the knowledge area frequency distribution, as presented in Figure 7.

The data detail specifically indicates the most covered knowledge area of software engineering by the articles selected in the study. Figure . 7, illustrates 3 most dominant knowledge areas presenting up to 46 studies identified on the knowledge areas of software development design and construction (33), project management ( 16), and quality (7). The remaining 31 studies covered the knowledge areas of process (5), models and methods (5), maintenance (4), testing (3), requirements (3) and management (1) with the respective number of studies. Although the knowledge areas that ultimately are observed at a point in time are presented decimally in the empirical literature, the initial 10 years show that these knowledge areas are not reflected in the empirical studies around this time. Figure 6(a) shows the studies in the years between 2016 and 2021 present interest in the knowledge area of quality, requirements, models and methods, and maintenance. Although the numbers are minimal, the growing interest of researchers is important for the industry and for the transformation of software development practice in SSCs. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 9)

### response

Software engineering adalah suatu disiplin yang terkait dengan berbagai fase produksi perangkat lunak dari pengumpulan persyaratan awal hingga pemeliharaan sistem perangkat lunak.

### reference


---

## Sample 2

- conversation_id: 13
- user_chat_id: 483
- bot_chat_id: 484

### user_input

Mengapa software engineering penting dalam pembuatan perangkat lunak?

### retrieved_context

1. In pursuance of the issues raised from the empirical literature, it is necessary for process theory to transform software engineering body of knowledge especially paying attention to SSCs. Additionally, research in software engineering has been predominately prescriptive and method-focused [39], producing thousands of software development methods that remain underutilized. In order to solve the challenges with software practice, practitioners and researchers should contribute to the body of knowledge [135], given that SSCs dominate the industry and are responsible for over 80% of software produced in the market. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

2. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

3. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. Software engineering is a discipline that is concerned with various phases of software production from the preliminary requirement gathering stage through to maintenance of the software system. It is therefore concluded that software engineering is a discipline that leads to a systematic approach where cost effective software development is performed. Regardless of the speedy progress, the software industry is well thought-out by several to be in a crisis. At that time the average software projects exceed the schedule by half. Similarly, large number of projects were either not functioning as expected or were not used at all. There are numerous other challenges, industry needs to deal with, if it continued to step forward for much more mature engineering discipline. Varying situational contexts among team members are one of the many challenges that can lead to failure software if left unattended. Software engineering standards significantly acknowledge the importance of situational contexts. In this study we have investigated the IEEE standards association for the relevant standards. We found 32 most relevant stanafter performing filtration on the data set. We concluded that these software engineering standards significantly acknowledge towards consideration of situational contexts for successful software. Each standard is investigated for the various factors and sub-factors that can lead to varying situational contexts among software engineering team members. Based upon the analysis, we came across a pattern in the identified standards. We reported 8 categories under which these standards are grouped. Each of the standard reports the factors and sub-factors related to its category. The identified factors are 12 in number. Each of them is further grouped with the related sub-factors (52 in number) that ultimately can lead to failure software if not addressed properly. This study provides a guideline for the practitioners to consider these factors and sub-factors while performing software development in order to have a successful software development. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 11)

5. From SWEBOK ISO/IEC TR 1975:2015, we adopt the critical knowledge areas in software engineering to use as synonyms for software engineering. Twelve knowledge areas identified from the keywords were selected as most prevalent in the literature. These include software requirements, software design, software construction, software maintenance, software testing, software configuration management, software management, software process, software models and methods, and software quality. This is seen in similar SMSs in software engineering by other researchers Klotins et al. [40]. These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

6. Software requirements outline the purpose of the development and design. It serves as the foundation of software intended to develop [1]. Requirements are defined in the beginning and act as a developmental milestones to accomplish successful executable software components [2]. Software requirement engineering is a systematic approach that is significantly developed in the course of the most recent decade [3]- [5]. Software architecture can be viewed as an organization of a system that comprehensively includes components interactions, operational environments, design principles, software functionalities, and often covers future evolutionary software perspective [6]- [9]. (Integration of Software Architecture in Requirements Elicitation for Rapid Software Development, page 1)

7. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

8. The use of measurement is common in all aspects of human life such as scales for buying vegetables, fruits, grocery items, gold or making estimations for reaching to the home of a friend. The applications of measurement are obvious in all disciplines such as sciences, engineering, medical and others. The measurements play a vital role in software organizations for the improvement of software processes [1], [2]. It is reported by many software quality assurance agencies that the quality of software product is strongly influenced by the quality of software process followed to develop the software product [3]. Software measurement has become an essential process in software organizations for characterizing, evaluating, predicting and improving software products, processes, and resources [4]- [6]. ISO/IEC 15939:2007 [4] defines measurement process as ''a process for establishing, planning, performing and evaluating measurement within an overall project, enterprise or organizational measurement structure''. Despite the acknowledged importance and advocated benefits of measurement processes for software engineering community, their actual applications in the software industry are limited [4], [5], [8], [9]. It is also reported in a systematic review on measurements in software engineering that software process is the least measured entity [35]. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

### response

Software engineering penting dalam pembuatan perangkat lunak karena dapat memastikan bahwa data dan layanan tidak terganggu (CIA: Confidentiality, Integrity, dan Availability). Selain itu, software engineering juga dapat membantu mengurangi biaya pengembangan perangkat lunak dan meningkatkan kualitasnya.

### reference


---

## Sample 3

- conversation_id: 13
- user_chat_id: 485
- bot_chat_id: 486

### user_input

Apa tujuan utama software engineering?

### retrieved_context

1. Software requirements outline the purpose of the development and design. It serves as the foundation of software intended to develop [1]. Requirements are defined in the beginning and act as a developmental milestones to accomplish successful executable software components [2]. Software requirement engineering is a systematic approach that is significantly developed in the course of the most recent decade [3]- [5]. Software architecture can be viewed as an organization of a system that comprehensively includes components interactions, operational environments, design principles, software functionalities, and often covers future evolutionary software perspective [6]- [9]. (Integration of Software Architecture in Requirements Elicitation for Rapid Software Development, page 1)

2. Over the recent decades of the last century, SA has emerged as the initial comprehension of the large-scope structures of software systems. SA is a collection of the primary design decision made throughout the period of development. Architecture is regarded as a core of software engineering that most accurately specifies the heart of software systems design and development [9]. Accomplishing non-functional and functional requirements is one of the most widely provided parts by SA since it is an integral part of the life-cycle of software evolution [22]. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 3)

3. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

5. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

6. The software engineering industry is undergoing a rapid transformation driven by the emergence of large language models (LLMs) and their use to create autonomous agents that can perform complex software engineering tasks. This paradigm shift, which we call agentic software engineering (ASE), represents a significant rethinking of how software is designed, developed, and maintained [1], [2], [3]. In contrast to traditional software engineering practices that rely primarily on human developers following established methodologies, ASE advocates the use of AI-based agents that have the autonomy to make decisions, write software, run tests, and interact throughout the software engineering lifecycle-a change reflected in recent work on LLM-based applications in software engineering [4], [5], [6], [7]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 1)

7. In pursuance of the issues raised from the empirical literature, it is necessary for process theory to transform software engineering body of knowledge especially paying attention to SSCs. Additionally, research in software engineering has been predominately prescriptive and method-focused [39], producing thousands of software development methods that remain underutilized. In order to solve the challenges with software practice, practitioners and researchers should contribute to the body of knowledge [135], given that SSCs dominate the industry and are responsible for over 80% of software produced in the market. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

8. From SWEBOK ISO/IEC TR 1975:2015, we adopt the critical knowledge areas in software engineering to use as synonyms for software engineering. Twelve knowledge areas identified from the keywords were selected as most prevalent in the literature. These include software requirements, software design, software construction, software maintenance, software testing, software configuration management, software management, software process, software models and methods, and software quality. This is seen in similar SMSs in software engineering by other researchers Klotins et al. [40]. These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

### response

Menurut konteks [Source: Integration of Software Architecture in Requirements Elicitation for Rapid Software Development], tujuan utama software engineering adalah sebagai berikut:

* Menyediakan dasar untuk pengembangan dan desain software
* Mencapai milestones pengembangan yang sukses dengan komponen software eksekutif

### reference


---

## Sample 4

- conversation_id: 13
- user_chat_id: 487
- bot_chat_id: 488

### user_input

Bagaimana software engineering membantu proses software development?

### retrieved_context

1. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

2. In pursuance of the issues raised from the empirical literature, it is necessary for process theory to transform software engineering body of knowledge especially paying attention to SSCs. Additionally, research in software engineering has been predominately prescriptive and method-focused [39], producing thousands of software development methods that remain underutilized. In order to solve the challenges with software practice, practitioners and researchers should contribute to the body of knowledge [135], given that SSCs dominate the industry and are responsible for over 80% of software produced in the market. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

3. Software engineering is a discipline that is concerned with various phases of software production from the preliminary requirement gathering stage through to maintenance of the software system. It is therefore concluded that software engineering is a discipline that leads to a systematic approach where cost effective software development is performed. Regardless of the speedy progress, the software industry is well thought-out by several to be in a crisis. At that time the average software projects exceed the schedule by half. Similarly, large number of projects were either not functioning as expected or were not used at all. There are numerous other challenges, industry needs to deal with, if it continued to step forward for much more mature engineering discipline. Varying situational contexts among team members are one of the many challenges that can lead to failure software if left unattended. Software engineering standards significantly acknowledge the importance of situational contexts. In this study we have investigated the IEEE standards association for the relevant standards. We found 32 most relevant stanafter performing filtration on the data set. We concluded that these software engineering standards significantly acknowledge towards consideration of situational contexts for successful software. Each standard is investigated for the various factors and sub-factors that can lead to varying situational contexts among software engineering team members. Based upon the analysis, we came across a pattern in the identified standards. We reported 8 categories under which these standards are grouped. Each of the standard reports the factors and sub-factors related to its category. The identified factors are 12 in number. Each of them is further grouped with the related sub-factors (52 in number) that ultimately can lead to failure software if not addressed properly. This study provides a guideline for the practitioners to consider these factors and sub-factors while performing software development in order to have a successful software development. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 11)

4. Software development is a collaborative activity, each member of the team has a certain set of responsibilities and tasks allocated to them, success of the software project depends on how these individuals contribute to the project. The human factor associated with these individuals makes it necessary to have a working environment that is diverse, equitable and inclusive to be productive. An organization which is diverse, equitable and inclusive has some social advantages such as higher employee engagement, productivity, higher job satisfaction, lower turnover, increased creativity, and reducing conflicts etc. which ultimately have the potential to increase the success of software projects. The challenge with the software engineering community is that the focus is always on the process side of the development, and little focus on the people who do the process. This study also reinforces this notion that evidence of comprehensive studies about practicing EDI in software development teams is limited, up to date majority focus is on the topic of diversity, whereas research on topics of practicing equity and inclusion in software development teams is sporadic and requires more attention. (Practicing Equity Diversity Inclusion (EDI) in Software Development Teams: A Systematic Literature Survey, page 1)

5. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

6. Perceived effectiveness (PE) refers to ''the degree to which using a technology will provide benefits to consumers in performing certain activities'' [51]. In terms of SE, research indicated that PE is an essential factor in studying the distributed requirements engineering [52]. It is also pointed out that PE had a positive influence on metamodeling acceptance [47] and computer-aided software engineering technology [53]. In this study, it is suggested that the higher the effectiveness of SBSET, the higher the usefulness of SBSET would be. Therefore, this leads to the following hypothesis: (The Acceptance of Search-Based Software Engineering Techniques: An Empirical Evaluation Using the Technology Acceptance Model, page 1)

7. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

8. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

### response

Software engineering membantu proses software development dengan:

* Menggunakan teknik AI untuk mendeteksi kelemahan dalam fase-fase SE dan mengirimkan peringatan tentang masalah tersebut.
* Membantu tim pengembang dengan menganalisis data proyek dan memberikan rekomendasi tindakan.
* Mendukung prioritas usaha dan memotong biaya inspeksi dan tes.

Informasi lebih lanjut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 5

- conversation_id: 13
- user_chat_id: 489
- bot_chat_id: 490

### user_input

Bagaimana software engineering berhubungan dengan software quality?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

3. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

4. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

5. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

6. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

7. TABLE 4. Path coefficients.

Analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS) telah membawa beberapa temuan penting. Data yang dianalisis menunjukkan bahwa ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan.

Kemudian, hasil analisis menunjukkan bahwa kualitas perangkat lunak merupakan faktor yang sangat penting dalam mempengaruhi kesuksesan COSS. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. Hasil ini dapat dijadikan sebagai rujukan bagi pihak manajemen dan strategis dalam mengembangkan kebijakan yang lebih efektif untuk meningkatkan kinerja perusahaan open-source software mereka. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 7)

8. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

### response

Software engineering memiliki peran penting dalam menentukan kualitas perangkat lunak. Perangkat lunak berkualitas dipengaruhi oleh efektifnya koordinasi proses pengembangan perangkat lunak dan kegiatan manajemen kualitas (engineering).

### reference


---

## Sample 6

- conversation_id: 13
- user_chat_id: 491
- bot_chat_id: 492

### user_input

Mengapa software engineering dibutuhkan untuk software maintenance?

### retrieved_context

1. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

2. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

3. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

5. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

6. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

7. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

8. Software engineering is a discipline that is concerned with various phases of software production from the preliminary requirement gathering stage through to maintenance of the software system. It is therefore concluded that software engineering is a discipline that leads to a systematic approach where cost effective software development is performed. Regardless of the speedy progress, the software industry is well thought-out by several to be in a crisis. At that time the average software projects exceed the schedule by half. Similarly, large number of projects were either not functioning as expected or were not used at all. There are numerous other challenges, industry needs to deal with, if it continued to step forward for much more mature engineering discipline. Varying situational contexts among team members are one of the many challenges that can lead to failure software if left unattended. Software engineering standards significantly acknowledge the importance of situational contexts. In this study we have investigated the IEEE standards association for the relevant standards. We found 32 most relevant stanafter performing filtration on the data set. We concluded that these software engineering standards significantly acknowledge towards consideration of situational contexts for successful software. Each standard is investigated for the various factors and sub-factors that can lead to varying situational contexts among software engineering team members. Based upon the analysis, we came across a pattern in the identified standards. We reported 8 categories under which these standards are grouped. Each of the standard reports the factors and sub-factors related to its category. The identified factors are 12 in number. Each of them is further grouped with the related sub-factors (52 in number) that ultimately can lead to failure software if not addressed properly. This study provides a guideline for the practitioners to consider these factors and sub-factors while performing software development in order to have a successful software development. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 11)

### response

Informasi tentang mengapa software engineering dibutuhkan untuk software maintenance tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 7

- conversation_id: 13
- user_chat_id: 493
- bot_chat_id: 494

### user_input

Bagaimana software engineering membantu mengurangi kesalahan dalam software testing?

### retrieved_context

1. Object-oriented metrics have been empirically validated to predict design flaws. Large and complex software systems are usually faulty [11]. It is difficult to keep them away from faults or to decrease risk of faults in upcoming version. According to [75], focus of verification and verification activities is to classify and remove high-risk problems in software. In order to avoid or squeeze faults, quality control models for example fault-prone models can be used for prediction of classes likely to be faulty. In order to attain these objectives, several researchers studied faults in software and constructed fault-proneness models base, on the event of failure [10], [34], [47], [76], [77]. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

2. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

3. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

4. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

5. Software standards can help to deal with software failures [5]. There are numerous standards regarding software engineering. Some of those standards are generic and some are specific towards any industry. Likewise, some of the standards are initiated from procurement agencies and others are either developed by certified bodies or related to certain software categories [6]. These standards comprehensively highlight the factors that can lead to varying situations [4]. These factors should be carefully considered during software development for resisting software failures [4].

In this study, we have reviewed various software engineering standards to investigate the situational factors that can lead to varying situations among software development team members.

Remaining paper comprises of five sections. Section II reports the research background. Section III discusses the research method used to recognize the situational factors. Section IV specifies the IEEE standards. Section V discusses the research elaborating the findings and future work. Section VI discusses the findings. Section VII elaborates some future work that can extend this research. Section VIII reports the limitations of this study, and Section IX concludes the research. (Software Standards and Software Failures: A Review With the Perspective of Varying Situational Contexts, page 1)

6. Software fault prediction process typically involves two phases which are denoted as training phase and the second is prediction phase where in the first phase, a model for prediction is constructed, which utilizes method or class level metrics of software with fault information associated with every single module of the software. Later, the same model is used to predict faulty classes in a new version of the software. SFP is effective to enhance the quality of software along with reducing the cost of testing. Also, it assists testing teams to limit testing on faulty classes only. Fault prediction in software possibly lays down yardstick for knowing, which areas may require attention. Many software fault prediction methods have been utilized [29], which contribute to three main elements [30]; Set of features, Label of Class, and finally the Model. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 3)

7. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

8. As time progresses and technology continues to develop, software has become an increasingly integral part of our daily lives. It is crucial that software functions correctly for endusers, making the assessment of software reliability a critical step in the testing phase. To accurately predict software reliability, various SRGMs have been proposed to describe the process of fault detection and correction [1], [2], [3]. It is important to note that there are still many SRGMs published in the literature. These models vary in terms of their underlying assumptions, mathematical formulations, and applicability to different types of software systems. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

### response

Software engineering dapat membantu mengurangi kesalahan dalam software testing dengan menggunakan berbagai metrik dan model prediksi kerusakan. Misalnya, dengan menggunakan inheritance metrics, developers dapat memprediksi kemungkinan kerusakan pada kelas-kelas tertentu dan meningkatkan kualitas software secara efektif. Selain itu, software standards juga dapat membantu mengurangi kesalahan dalam software testing dengan memberikan pedoman yang jelas tentang bagaimana melakukan pengujian dan analisis keamanan.

Dengan demikian, software engineering berperan penting dalam meningkatkan kualitas software dan mengurangi kemungkinan kerusakan selama fase pengujian.

### reference


---

## Sample 8

- conversation_id: 13
- user_chat_id: 495
- bot_chat_id: 496

### user_input

Apa peran software metrics dalam software engineering?

### retrieved_context

1. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

6. TABLE 2. Frequently Used Metrics in Software Fault Prediction.

Tabel ini memuat beberapa studi terkait penggunaan metrik dalam prediksi kegagalan perangkat lunak. Lima belas penelitian yang disebutkan menunjukkan bahwa beberapa metrik telah digunakan secara luas dalam prediksi kegagalan, seperti metrik yang terkait dengan sifat objek-oriented dan perilaku pengguna.

Variabel utama di tabel ini meliputi nama penulis, judul penelitian, metode yang digunakan, serta hasil yang diperoleh. Nilai penting dari tabel ini adalah penemuan bahwa beberapa metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak.

Pola penting dapat dilihat dari kemunculan istilah-istilah seperti "C&K metrics" dan "Li and Henry," yang mengindikasikan bahwa ada metrik yang secara konsisten digunakan dalam penelitian-penelitian ini. Selain itu, juga terlihat bahwa beberapa penulis menggunakan kombinasi berbagai metode analisis untuk mencapai hasil prediksi yang lebih akurat.

Insight singkat dari tabel ini adalah pentingnya penggunaan metrik-metrik tertentu dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 13)

7. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

8. The use of measurement is common in all aspects of human life such as scales for buying vegetables, fruits, grocery items, gold or making estimations for reaching to the home of a friend. The applications of measurement are obvious in all disciplines such as sciences, engineering, medical and others. The measurements play a vital role in software organizations for the improvement of software processes [1], [2]. It is reported by many software quality assurance agencies that the quality of software product is strongly influenced by the quality of software process followed to develop the software product [3]. Software measurement has become an essential process in software organizations for characterizing, evaluating, predicting and improving software products, processes, and resources [4]- [6]. ISO/IEC 15939:2007 [4] defines measurement process as ''a process for establishing, planning, performing and evaluating measurement within an overall project, enterprise or organizational measurement structure''. Despite the acknowledged importance and advocated benefits of measurement processes for software engineering community, their actual applications in the software industry are limited [4], [5], [8], [9]. It is also reported in a systematic review on measurements in software engineering that software process is the least measured entity [35]. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 1)

### response

Software metrics berperan sebagai dasar untuk mengukur kompleksitas, kualitas perangkat lunak, dan perkiraan biaya serta upaya proyek. Mereka juga digunakan untuk menilai efisiensi dan keamanan sistem software. Fungsi point dan cyclomatic complexity adalah contoh metrik tradisional yang digunakan dalam paradigm prosedural, tetapi tidak dapat secara langsung diaplikasikan pada paradigma berorientasi objek.

Beberapa studi telah menunjukkan bahwa penggunaan metrik khususnya terkait dengan sifat objek-oriented telah terbukti efektif dalam prediksi kegagalan perangkat lunak. Dengan demikian, penelitian ini menunjukkan bahwa dengan memahami dan menggunakan metrik yang tepat, kita dapat meningkatkan akurasi prediksi kegagalan perangkat lunak.

Sumber: [Source: Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper], [Source: Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction]

### reference


---

## Sample 9

- conversation_id: 13
- user_chat_id: 497
- bot_chat_id: 498

### user_input

Bagaimana Agile software development mempengaruhi praktik software engineering?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. The software engineering industry is undergoing a rapid transformation driven by the emergence of large language models (LLMs) and their use to create autonomous agents that can perform complex software engineering tasks. This paradigm shift, which we call agentic software engineering (ASE), represents a significant rethinking of how software is designed, developed, and maintained [1], [2], [3]. In contrast to traditional software engineering practices that rely primarily on human developers following established methodologies, ASE advocates the use of AI-based agents that have the autonomy to make decisions, write software, run tests, and interact throughout the software engineering lifecycle-a change reflected in recent work on LLM-based applications in software engineering [4], [5], [6], [7]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 1)

3. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

4. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

5. FIGURE 6. Frequency of adapted software development standard.

Gambar ini menampilkan sebuah grafik batang yang berisi informasi tentang frekuensi penggunaan standar pengembangan perangkat lunak (software development standard) oleh para pengembang. Grafik tersebut membagi data menjadi beberapa kategori, masing-masing dengan warna yang berbeda.

Grafik menunjukkan bahwa kategori dengan frekuensi tertinggi adalah "Agile" dengan warna hijau. Kemudian diikuti oleh "Waterfall" dengan warna biru, dan terakhir ada "Kanban" dengan warna kuning.

Angka yang paling mencolok adalah 40% untuk kategori "Agile". Ini berarti bahwa 40% dari responden pengembang perangkat lunak menggunakan standar Agile dalam pengembangan proyek mereka. Angka ini mungkin menunjukkan bahwa banyak pengembang memilih untuk menggunakan metodologi Agile karena fleksibilitas dan kemampuannya untuk mendukung kerja sama tim.

Makna singkat dari gambar ini adalah bahwa para pengembang perangkat lunak memiliki preferensi yang beragam dalam hal standar pengembangan. Namun, metodologi Agile terlihat menjadi pilihan populer karena ketersediaan dan keleluasaannya dalam menghadapi tantangan pengembangan perangkat lunak yang kompleks. (An Evaluation of Software Measurement Processes in Pakistani Software Industry, page 8)

6. Agentic software engineering is a major development in the design, development, and maintenance of software systems, and its effects extend beyond the simple automation of existing processes. The accelerated development as can be seen in the literature that shows a shift of mere aids to complex autonomous multi-agent systems points out to the fact that the transformation is gaining momentum and is likely to go on redefining the software development environment. Despite the significant difficulties that still remain to be addressed, especially in the following aspects coordination protocols, security systems, evaluation systems, and patterns of human-agent collaboration, the potential gains in the form of productivity enhancement, quality improvement, and accessibility expansion are absolutely convincing and warrant continued expenditure of resources on research and development. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 20)

7. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

8. The software industry has experienced rapid expansion in recent years, with software development now essential to the success of many multinational corporations. The demand for complex software systems has dramatically increased, effective software development has become crucial, given the limitations of resources such as money, time, and labor. Cost and effort calculations significantly impact the development process and client needs, and project failure is often caused by errors in job estimating. Underestimating a project's cost and effort can have severe repercussions, such as exceeding the project's budget. Project overruns, on the other hand, can also have a detrimental impact on software projects' successful completion. Researchers and experts in the software industry are continually exploring ways to keep management and development productivity at high levels. However, standalone estimating models have revealed inadequacies over the last decade, and they have not produced any noteworthy research results. Recent literature suggests that opting for ensemble models would yield better results than standalone models. We have proposed a heterogeneous ensemble effort estimation (EEE) model in this research. Our proposed model comprises standalone estimating models such as Use Case Point, Expert Judgment (EJ), and Artificial Neural Network (ANN). We combined the effort of each unique base model using linear combination rule. To validate our model's effectiveness, we applied it to the benchmark dataset, the International Software Benchmarking Standards Group (ISBSG), using three different variations to avoid biases. We further applied the trained models to industry use cases for cross-validation. Our study's findings demonstrated that, in comparison to stand-alone estimate strategies, the ensemble technique produced better estimation results. Finally, our study proposes a heterogeneous ensemble effort estimation model that outperforms standalone models in terms of accuracy. This model has the potential to aid in effective software development, particularly in project cost and effort estimation. INDEX TERMS Software effort estimation, ensemble effort estimation (EEE), standalone estimation, use case point (UCP), machine learning algorithms, deep learning, expert judgement. (Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy, page 1)

### response

Agile software development telah membawa perubahan signifikan dalam praktik software engineering. Secara khusus, itu telah menyebabkan peningkatan fleksibilitas dan kemampuan untuk beradaptasi dengan perubahan pasar yang cepat. Praktik Agile seperti integrasi kontinu [29] memberikan koneksi erat dengan pengembangan untuk memastikan bahwa kesalahan dapat dideteksi dan diperbaiki secepat mungkin.

Kemampuan ini telah meningkatkan potensi analitis software, yang sangat penting dalam memenuhi kebutuhan pelanggan yang dinamis. Selain itu, Agile juga telah membantu mengurangi waktu pengembangan produk dan meningkatkan kualitas produk.

### reference


---

## Sample 10

- conversation_id: 13
- user_chat_id: 499
- bot_chat_id: 500

### user_input

Bagaimana software engineering membantu menjaga sistem CNN agar mudah dipelihara?

### retrieved_context

1. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

2. Secure Software Engineering (SSE) has become a significant paradigm in the development of secure software for the software industry in recent years as security problems in the SDLC are difficult to address. Information and Communication Technology (ICT) has undeniably changed human lives, communications, the digital economy, socialization, and entertainment. Similarly, the market for internet-enabled applications is increasingly increasing. Therefore, there is an ever-growing demand for trusted software applications. Software security is the key to the software's success, especially in The associate editor coordinating the review of this manuscript and approving it for publication was Luca Cassano. today's fast-paced and technology-oriented world. Software and technology have become such an inseparable part of our lives that it's virtually impossible to imagine a sector that doesn't employ them in its day-to-day operations. The world in every aspect has been modernized by an immense use of software systems. Software security ensures that the CIA (Confidentiality, Integrity, and Availability) of data and services are not compromised [1], [2]. This can only be done if the security is considered during all SDLC phases [1], [2]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

3. Nuclear power plants (NPPs) employ several safety systems to protect the public from the release of radioactive material in case of an accident. These safety systems are manipulated by the instrumentation and control (I&C) systems, which provide the control and monitoring functions of the various and diverse components and equipment that are essential to maintain safe operation. Existing I&C systems are currently being replaced with microprocessor-based digital systems because of the obsolescence of analog-based I&C equipment and a lack of vendor support. It is true that digital systems provide better performance such as improved accuracy, computation capabilities, and data handling, as well as the potential for improved capabilities such as fault tolerant techniques [1]. (Input-Domain Software Testing for Failure Probability Estimation of Safety-Critical Applications in Consideration of Past Input Sequence, page 1)

4. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

[39] TJ Bosch, T Hanna, KA Fercho, LA Baugh. Behavioral performance and visual strategies during skill acquisition using a novel tool use motor learning task. (2018-12)

[40] W Choi. The effect of task-oriented training on upper-limb function, visual perception, and activities of daily living in acute stroke patients: A pilot study. (2022-03)

[41] I Pysmennyi, R Kyslyi, A Petrenko. Edge computing in multi-scope service-oriented mobile healthcare systems. (2019-03)

[42] J Lv, Q Sun, Q Li, L Moreira-Matias. Multi-scale and multiscope convolutional neural networks for destination prediction of trajectories. (2020-08)

[43] AA Saputra, K Wada, S Masuda, N Kubota. Multi-scopic neuro-cognitive adaptation for legged locomotion robots. (2021-08)

[44] AF Zhu, P Rahgozar, KC Chung. Advances in proximal interphalangeal joint arthroplasty. (2018-05)

[45] J.-S Won, S Lee. Geometry-based finger kinematic models for joint rotation configuration and parameter estimation. (2020-07)

[46] AR A Besari, AA Saputra, WH Chin, N Kubota, Kurnianingsih. Feature-based egocentric grasp pose classification for expanding humanobject interactions. (2021-06)

[47] PB Shull, S Jiang, Y Zhu, X Zhu. Hand gesture recognition and finger angle estimation via wrist-worn modified barometric pressure sensing. (2019-04)

[48] I Imbinto, F Montagnani, M Bacchereti, C Cipriani, A Davalli, R Sacchetti, E Gruppioni, S Castellano, M Controzzi. The S-finger: A synergetic externally powered digit with tactile sensing and feedback. (2018-06)

[49] J Mazumder, LN Nahar, M Md Uddin Atique. Finger gesture detection and application using hue saturation value. (2018-08)

[50] WB Dou, WH Chin, N Kubota. Hand gesture communication using deep learning based on relevance theory,'. (2020-12)

[51] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[52] Y Cheng. Backpropagation for fully connected cascade networks. (2017-08)

[53] P Gajbhiye, N Mingchinda, W Chen, SC Mukhopadhyay, T Wilaiprasitporn, RK Tripathy. Wavelet domain optimized Savitzky-Golay filter for the removal of motion artifacts from EEG recordings. (2021)

[54] R Chen, M Wang, J.-H Chang. A study of the pinch performance and subjective satisfaction with chopsticks of different lengths. (2017)

[55] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[56] YJ R De Kloe, IT C Hooge, C Kemner, DC Niehorster, M Nyström, RS Hessels. Replacing eye trackers in ongoing studies: A comparison of eye-tracking data quality between the Tobii pro TX300 and the tobii pro spectrum. (2022-01)

[57] EP Larsen, JM Kolman, FN Masud, F Sasangohar. Ethical considerations when using a mobile eye tracker in a patient-facing area: Lessons from an intensive care unit observational protocol. (2020-11)

[58] DC Niehorster, T Santini, RS Hessels, IT C Hooge, E Kasneci, M Nyström. The impact of slippage on the data quality of head-worn eye trackers. (2020-06)

[59] C Chen, W Guo, C Ma, Y Yang, Z Wang, C Lin. SEMGbased continuous estimation of finger kinematics via large-scale temporal convolutional network. (2021-05)

[60] C Dai, X Hu. Finger joint angle estimation based on motoneuron discharge activities. (2020-03)

[61] H Eschmann, ME Héroux, JH Cheetham, S Potts, J Diong. Thumb and finger movement is reduced after stroke: An observational study. (2019-06)

[62] SN Emhardt, M Wermeskerken, K Scheiter, T Gog. Inferring task performance and confidence from displays of eye movements. (2020-11)

[63] X Fang, F Yu, G Yang, Y Qu. Regression analysis with differential privacy preserving. (2019)

[64] H Zhu, X You, S Liu. Multiple ant colony optimization based on Pearson correlation coefficient. (2019)

[65] L Ke, A Kamat, J Wang, T Bhattacharjee, C Mavrogiannis, SS Srinivasa. Telemanipulation with Chopsticks: Analyzing human factors in user demonstrations. (2022-06)

[66] A Murata, T Doi, W Kageyama, Karwowski. Development of an eye-gaze input system with high speed and accuracy through target prediction based on homing eye movements. (2021)

[67] B Banire, D Al-Thani, M Qaraqe, K Khowaja, B Mansoor. The effects of visual stimuli on attention in children with autism spectrum disorder: An eye-tracking study. (2020) (Finger Joint Angle Estimation With Visual Attention for Rehabilitation Support: A Case Study of the Chopsticks Manipulation Test, page 2)

5. FIGURE 9. CNN model training result.

Gambar ini menampilkan grafik hasil pelatihan model CNN (Convolutional Neural Network). Grafik ini terlihat seperti garis di atas yang menunjukkan proses pengembangan akurasi model CNN selama proses pelatihan. Pada awalnya, akurasi model cukup rendah, tetapi kemudian meningkat secara signifikan seiring dengan berjalannya waktu dan iterasi pelatihan.

Pada grafik tersebut terdapat beberapa titik tertentu yang menunjukkan peningkatan drastis dalam akurasi. Meskipun tidak ada angka spesifik yang dapat diidentifikasi, namun jelas bahwa model CNN telah berhasil meningkatkan akurasinya hingga mencapai nilai yang sangat tinggi.

Dari grafik ini kita dapat menyimpulkan bahwa proses pelatihan model CNN telah berjalan dengan efektif dan akurasi model meningkat secara signifikan. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

6. As a result, there are numerous research reports made by the academy. As it can be noticed, SBSET allows to reduce software design time, decrease the cost of software testing and maintenance, and therefore, it can produce more reliable software. It is also anticipated that SBSET can help avoiding error-prone work in the different aspects of software engineering process. (The Acceptance of Search-Based Software Engineering Techniques: An Empirical Evaluation Using the Technology Acceptance Model, page 2)

7. Maintainability is the ease with which an AI-based software can be modified, updated, or extended to adapt to changing requirements or environments. This involves aspects such as modularity, reusability, and simplicity of the AI models and codebase. Ensuring maintainability in AI systems requires careful design, adherence to best practices, and documentation of the AI model architecture and development process. Maintainability can be assessed using code-level metrics such as cyclomatic complexity, lines of code, code duplication, and code coverage. For AI systems, the modularity and reusability of model components can also be considered, along with the adherence to best practices and coding standards. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 10)

8. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

### response

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 11

- conversation_id: 13
- user_chat_id: 501
- bot_chat_id: 502

### user_input

Apa itu software quality?

### retrieved_context

1. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

2. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

3. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

4. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

5. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

6. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

7. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

8. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

* Totalitas dari karakteristik suatu entitas yang terkait dengan kemampuannya untuk memenuhi kebutuhan yang telah ditetapkan dan implisit.
* Kemampuan suatu sistem software untuk memenuhi kombinasi kualitas atribut yang diinginkan (kompleksitas, keandalan, skalabilitas, fungsi, efisiensi, portabilitas, usability, dan maintainability).
* Kapasitas suatu entitas untuk memenuhi kebutuhan eksplisit dan implisit.
* Totalitas dari karakteristik suatu entitas yang terkait dengan kemampuannya untuk memenuhi kebutuhan yang telah ditetapkan dan implisit.

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 12

- conversation_id: 13
- user_chat_id: 503
- bot_chat_id: 504

### user_input

Mengapa software quality penting?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. Quality is the most important factor for software development as it mainly defines customer satisfaction that is directly related to the success of a software project. The software process model is used to ensure software quality, represent a variety of task settings, manage project duration, improve the process and range to execute the process understanding, and to appropriate implicit conjecture for all task settings. Several software processes models exist in software albeit with limited scope. Given this viewpoint, this paper presents a new software development life cycle model, ''AZ-Model,'' for software development by introducing new activities during software development life cycle. It overcomes the limitations of traditional models and significantly impacts the production of a quality product in a time-box. This paper also presents a comprehensive comparative study and statistical analyses to examine the significance of AZ-Model for software development. INDEX TERMS Software development model (SDM), project management (PM), AZ-Model, software development life cycle (SDLC), six pointed star model, project management factors. (Improving the Quality of Software Development Process by Introducing a New Methodology–AZ-Model, page 1)

3. The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1]. Although the products produced by the SSCs fail to meet the expected quality, software is still central in influencing human activity. Recent studies indicate that most aspects of society depend on software; moreover, SSCs are responsible for up to 80 percent of software produced on the market. The contribution of SSCs cannot be underestimated since they represent up to 90 percent of software companies in the industry [2]. (Theory on Non-Technical Characteristics Affecting Process Adoption in Small Software Companies: A Grounded Theory Study, page 1)

4. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

5. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

6. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

7. Quality of a software product is an intransigence factor. For executable software components, quality comes first and foremost. Addressing quality requirements has always been a challenge for the requirement engineering process and software designing phase [77]. To focus functional requirements of the system, a better designing approach integrating architectural perspective is required along with suitable skills, tools, and techniques.

Quality attributes are the backbone for the success of the software artefacts. Traditionally, quality attributes like usability, reliability and other quality requirements are considered later stages of development that itself leads to late identification of flaws [78]. Therefore, software architecture is considered as favourable choice as it focuses on non-functional quality attributes along with functional requirements to make things smoother [78]. (Integration of Software Architecture in Requirements Elicitation for Rapid Software Development, page 8)

8. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

### response

Software quality penting karena:

* Ia memenuhi harapan pelanggan dan mendukung pertumbuhan organisasi.
* Ia merupakan faktor kesuksesan kritis untuk perusahaan pengembangan perangkat lunak.
* Ia terutama menentukan kepuasan pelanggan yang terkait dengan suksesnya proyek software.
* Software quality dapat dipengaruhi oleh biaya dan waktu batas, serta mempengaruhi kemampuan perangkat lunak untuk memenuhi kebutuhan pelanggan.
* Kualitas perangkat lunak juga mempengaruhi pemeliharaan perangkat lunak, kesepakatan ekonomi, dan kehidupan manusia di konteks nyata.

### reference


---

## Sample 13

- conversation_id: 13
- user_chat_id: 505
- bot_chat_id: 506

### user_input

Apa saja faktor yang mempengaruhi software quality?

### retrieved_context

1. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

2. The quality of software continues to be a significant challenge in the software industry, and this challenge is more visible in the Small Software Companies (SSCs) to the extent that up to 70 percent of software projects are challenged either due to defects, cost overruns or overshot scheduling related challenges [1]. Although the products produced by the SSCs fail to meet the expected quality, software is still central in influencing human activity. Recent studies indicate that most aspects of society depend on software; moreover, SSCs are responsible for up to 80 percent of software produced on the market. The contribution of SSCs cannot be underestimated since they represent up to 90 percent of software companies in the industry [2]. (Theory on Non-Technical Characteristics Affecting Process Adoption in Small Software Companies: A Grounded Theory Study, page 1)

3. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

4. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

5. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

6. TABLE 4. Path coefficients.

Analisis terbaru mengenai komponen kualitas perangkat lunak (software quality) dalam menengahi dampak modal intelektual (intellectual capital) pada kesuksesan perusahaan swasta open-source software (COSS) telah membawa beberapa temuan penting. Data yang dianalisis menunjukkan bahwa ada hubungan positif signifikan antara kualitas perangkat lunak dan kesuksesan COSS (β = 0,581, T-value = 10,842, P-value = 0,000). Sebenarnya, kualitas perangkat lunak memainkan peran mediasi yang signifikan dalam menengahi hubungan antara modal intelektual dan kesuksesan COSS.

Penelitian ini juga menemukan bahwa ada hubungan positif antara kapital struktural (structural capital) dan kualitas perangkat lunak, serta antara kapital manusia (human capital) dan kualitas perangkat lunak. Dalam beberapa kasus, mediasi efektif kapital manusia pada relasi tersebut terbukti signifikan.

Kemudian, hasil analisis menunjukkan bahwa kualitas perangkat lunak merupakan faktor yang sangat penting dalam mempengaruhi kesuksesan COSS. Dengan demikian, penelitian ini mendukung asumsi-asumsi yang telah diusulkan (H1-H11) mengenai hubungan antara modal intelektual dan kualitas perangkat lunak terhadap kesuksesan COSS.

Dari hasil analisis, dapat disimpulkan bahwa kualitas perangkat lunak merupakan faktor penting dalam menengahi dampak kapital manusia terhadap kesuksesan COSS. Hasil ini dapat dijadikan sebagai rujukan bagi pihak manajemen dan strategis dalam mengembangkan kebijakan yang lebih efektif untuk meningkatkan kinerja perusahaan open-source software mereka. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 7)

7. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

8. Nowadays, a company's ability to innovate is increasingly driven by software. Digital technologies play a key role in The associate editor coordinating the review of this manuscript and approving it for publication was Waldemar W. Koczkodaj. the transformation of many industrial companies [1], especially in sectors like the automotive industry, where software (together with electronics) is responsible for over 90% of all innovations [2], [3]. In this context, software quality makes the difference and is an essential competitive factor for company success. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

Berikut adalah jawaban atas pertanyaan user berdasarkan konteks:

Faktor yang mempengaruhi software quality adalah:

• Biaya dan waktu keterbatasan (cost and time constraints) [12], [13], [42], [43]
• Koordinasi efektif dari proses pengembangan perangkat lunak dan kegiatan manajemen kualitas (effective coordination of software development processes and quality management activities)
• Kapital struktural (structural capital) [β = 0,581, T-value = 10,842, P-value = 0,000]
• Kapital manusia (human capital) [β = 0,581, T-value = 10,842, P-value = 0,000]

### reference


---

## Sample 14

- conversation_id: 13
- user_chat_id: 507
- bot_chat_id: 508

### user_input

Bagaimana software quality dapat diukur?

### retrieved_context

1. In order to effectively coordinate and evaluate software quality management efforts, software companies use software quality models [34], [37], [44], [45]. The earliest software quality model was proposed by McCall in 1976. The McCall model was later revised by Boehm and Dromey [41], [44], [46], [47]. Recently developed software quality evaluation models include ISO/IEC 25010 which outlines 8 attributes to be used for software quality assessment. In contrast, the earlier version ISO/IEC 9126 adopts 6 characteristics [44], [45], [48].

Despite being viewed as a useful tool for quality assurance [44], software standards or models lack functionality and practical application owing to the ambiguity involved [37], [47]. Gorla and Lin as cited in [49] propose a software quality assessment model that includes relevance and usefulness (i.e., functionality), usability, maintainability, and reliability attributes. On the other hand, other scholars identify usability, reliability, functionality, performance efficiency, portability, and maintainability as important quality measurements [40], [46]. Similarly, several studies identify functionality, usability, reliability, performance efficiency, and maintainability as the most impactful measures of software quality [14], [41], [43], [45]. Consequently, functionality, usability, performance efficiency, reliability, and maintainability indicators are adopted for the evaluation of software quality in this study. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 1)

2. Software quality is calculated in the following formula (4):  In formula (4), q is Software quality; b is Open bugs; l is Total changed codes. Software quality is expressed by the bug rate, which is equal to the number of Open bugs divided by the Total changed codes.

In Quality assurance subsystem, Code review by numerous reviewers, particularly when carried out in tandem with automatic test, can significantly, positively impact software quality. Code review in Figure 7 is a ratio of the effectiveness of the review. If it is equal to 0, it means that the changed code is not reviewed. In the following empirical case study (in Section III), we input a random function to analyze its impact. (Change-Oriented Open Source Software Process Simulation, page 1)

3. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

4. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

5. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

6. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

7. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

8. Software analytics is defined as ''analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight from their data to make better decisions'' [6]. In this context, analytics results should include some actionable knowledge that can be used to improve software quality. Software analytics is used in various scenarios to assess concrete problems, e.g., use of process data to predict overall project effort [26], use of security data to identify indicators for software vulnerabilities [27], or classification of app reviews [28]. In this context, software analytics tools provide features for specifically visualizing software development aspects. In our view, some notable examples are SonarQube, 11 Kiuwan, Bitergia, 12 and Tasktop, all of which have been discussed in related work. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

### response

Berikut adalah beberapa cara untuk mengukur software quality berdasarkan konteks yang disediakan:

* Dengan menggunakan formula (4): q = b / l, di mana q adalah Software quality, b adalah Open bugs, dan l adalah Total changed codes.
* Dengan memperhitungkan atribut-atribut kualitas seperti kompleksitas, keandalan, skala, fungsi, efisiensi, portabilitas, kemanfaatan, dan perawatan (maintainability).
* Dengan menggunakan standar ISO/IEC 25010 yang memiliki 8 atribut untuk mengevaluasi kualitas software.
* Dengan membandingkan hasil analisis data dengan standar kinerja yang ditetapkan.
* Dengan menggunakan alat-alat analytics seperti SonarQube, Kiuwan, Bitergia, dan Tasktop untuk mengukur kualitas software.

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 15

- conversation_id: 13
- user_chat_id: 509
- bot_chat_id: 510

### user_input

Apa hubungan software quality dengan software testing?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

3. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

4. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

5. Quality is defined by ISO 8042 [18] as ''the totality of characteristics of an entity that bear on its ability to satisfy stated and implied needs''. This definition is too abstract to be operationalized directly, and is one of the reasons why there has been a multitude of software QMs proposed in the last four decades (e.g., [15], [19]- [22]) that refine high-level concepts of ''quality'' (like reliability or efficiency) down to the level of metrics (as number of bugs or response time). One popular example widely adopted in industry is the ISO/IEC 25010 standard [14], which determines the quality aspects to be taken into account when evaluating the properties of a software product. Two more recent examples well known in industry are Quamoco and SQALE [23]. Quamoco [16] is a QM integrating abstract quality aspects and concrete quality measurements. SQALE [24] computes technical debt indexes based on the violations of quality rules in the source code. Other works propose refactoring models to improve a particular quality aspect of the existing model or code, and different extensions to the traditional concept of quality (such as incorporation of non-technical criteria into ISO/IEC 9126-1 QM [25]). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 1)

6. Barmi et al. conducted a systematic review to better understand the connections between the specifications and testing requirements and reported that ''Model-based testing'' was the most commonly studied topic (26%), followed by ''Formal Approaches'' (24%), and ''Traceability'' (18%) and concluded that there was a significant gap between the specification and testing requirements [31]. Their study is considering the relationship between the specifications and testing requirements, not the whole process of software testing. In this context, Garousi and Mäntylä reported that over 101 secondary research studies (as a study of studies) had been published in the area of software testing since 1994, with model-based software testing being the most popular method, web-services the most popular system, and regression testing the most popular testing phase [32]. Since this was a ternary study, it has limitations in showing the whole picture of the software testing studies. Zein et al. performed a systematic mapping study in order to reveal testing techniques for mobile application and mapped 79 empirical studies to a taxonomy [33]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

7. In the software testing stages, the aim is to develop softwareoriented products and services in a systematic and efficient manner, in which a wide range of tasks, methods, and strategies are used. Depending on the type, scope and context of the designed and developed, the methods and strategies  chosen during the software testing stages vary considerably. The findings of this study offer a wide-ranging insight into not only the themes and trends in focus but also the tools, tasks, methods, and strategies specific to software testing. Specifically, the discovered topics reveal that the most focused tasks in software testing are specification, transformation, detection, localization, generation, evaluation, optimization, verification, and prediction. The important background provided by the core tasks highlighted in this study for software testing has also been addressed by previous studies [49]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 9)

8. ''Testing AI software refers to diverse testing activities for AI-based software/systems. Well-defined quality validation models, methods, techniques, and tools must be developed and applied for AI-based software to facilitate the test activities to achieve well-defined test requirements and meet pre-selected adequate testing criteria and quality assurance standards.'' Therefore, testing AI features of the software includes different testing activities to find software errors, verify the performance of software, and assuring quality validation methods need to be developed. The testing goal is to achieve well-defined test requirements, meet pre-defined testing criteria, and standards of quality assurance of the under-test AI software. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

### response

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 16

- conversation_id: 13
- user_chat_id: 511
- bot_chat_id: 512

### user_input

Bagaimana software metrics digunakan untuk menilai software quality?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

6. The set of features are consisting of single or multiple metrics derived through artifacts of software, it is believed that these are useful to predict labels of class. All of the metrics are grouped into the product, project, and process metrics. It is observed that metrics of the product are mostly utilized in the research arena [31]. The further level of product metrics includes method, class, and file levels where overall 60% method-level metrics are utilized followed by 24% classlevel metrics [15]. Metrics of the product also consist of, volume, design, code, and complexity metrics. The performance of SFP heavily depends on these metrics. Researchers have assessed the utilization rate of metrics in [32] where highly use product metrics in software fault prediction are Halstead [1], McCabe [3], LoC in structural programming, and in object-oriented paradigm C&K metrics suite [33]. The subject metrics are become the approved standard metrics in software fault prediction. PROMISE and D'Ambros [34] are frequently used datasets repositories having these metrics. Both the repositories encompass datasets of about fifty-two percent of the research paper published after 2005 [9]. Since these datasets are publicly available therefore it is frequently used. The other reason is the non-availability of bug's data of industrial software. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 4)

7. Object-oriented metrics are used to predict the quality of object-oriented software. The attributes that determine software quality include maintainability, fault tolerance, understandability, fault density, standardized rework rate, reusability, etc. Several studies were carried out, including the empirical verification of the object-oriented metrics in open source software for the prediction of faults using CBO, LOC, LCOM, NOC and DIT [10], reuse analysis of objectoriented systems using metrics of inheritance, coupling and cohesion [92], heuristic review of CK metrics [93], reusable metrics for object-oriented design [94] and empirical analysis of CK metrics for object-oriented design complexity [95]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 5)

8. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Software metrics digunakan untuk menilai kualitas software dengan beberapa cara, antara lain:

* Menilai kompleksitas dan kualitas kode program
* Memprediksi kemungkinan adanya kerusakan (fault) dalam sistem
* Menganalisis perilaku atau fungsi sistem
* Mengukur efisiensi dan keamanan sistem

Dalam beberapa sumber, disebutkan bahwa software metrics dapat digunakan untuk menilai kualitas software melalui:

* Internal metrics: mengukur kualitas kode program
* Eksternal metrics: mengukur perilaku atau fungsi sistem
* Structural complexity measures: mengukur kompleksitas arsitektur sistem
* Quality metrics: mengukur keandalan sistem
* Productivity metrics: mengukur dampak alat bantu GAI terhadap kecepatan, kualitas, dan efisiensi pengembangan sistem.

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 17

- conversation_id: 13
- user_chat_id: 513
- bot_chat_id: 514

### user_input

Mengapa software quality perlu dijaga selama software maintenance?

### retrieved_context

1. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

2. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

3. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

4. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

5. In general, quality is considered as the most vital factor for meeting customer expectations and organizational growth [12], [34], [40]. More specifically, software quality is a critical success factor for software development companies [12], [13], [41]. Software development companies often depend on effective coordination of software development processes and quality management activities (engineering) to attain the desired level of software quality. In addition to effective coordination, software quality is also affected by cost and time constraints [12], [13], [42], [43]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 3)

6. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

7. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

8. Software quality is defined by how closely a software system meets a desired combination of quality attributes [6], [7]. These attributes include complexity, reliability, scalability, functionality, efficiency, portability, usability, and maintainability, each contributing to the system's overall effectiveness [8], [9]. These quality attributes reflect the actual characteristics of the implemented system [8].

In AI-based systems, quality attributes are critical in shaping architectural decisions [4]. These systems introduce additional challenges, such as model management, accuracy, robustness, and inference latency [3], which the architectural design process must carefully address. Consequently, selecting an appropriate architectural style ensures that AI-based software systems meet their requirements effectively. (Architectural Styles and Quality Attributes in AI-Based Video Software: A Systematic Literature Review, page 1)

### response

Jawaban:
Software quality perlu dijaga selama software maintenance karena hal ini dapat mempengaruhi kinerja, keamanan, dan keandalan sistem. Dengan menjaga software quality, masalah yang tidak terduga dapat dicegah dan biaya yang diperlukan untuk mengatasi masalah tersebut dapat diminimalkan.

Rujukan:
- [Source: How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success]
- [Source: Change-Oriented Open Source Software Process Simulation]
- [Source: Systematic Mapping: Artificial Intelligence Techniques in Software Engineering]

### reference


---

## Sample 18

- conversation_id: 13
- user_chat_id: 515
- bot_chat_id: 516

### user_input

Bagaimana Agile software development dapat membantu meningkatkan software quality?

### retrieved_context

1. Agile development methodologies are widely adopted nowadays by software development companies of every kind [37]. Industry surveys show that virtually all organisations use Agile methods to some extent, and over half of them have Agile as their usual approach to software development. 1 Practitioners report many benefits, ranging from reduced timeto-market, to increased customer satisfaction and reduced development costs, among others. 2 However, managing Agile projects may be challenging [10], especially in the case of Small and Medium Enterprises (SMEs). The challenge for the The associate editor coordinating the review of this manuscript and approving it for publication was Fabrizio Messina . 1 13th Annual State of Agile Report, 2019. https://www.stateofagile.com/#ufh-i-521251909-13th-annual-state-of-agile-report/473508 2 Hewlett-Packard Enterprise. Agile is the new normal, 2015. https://www.softwaretestinggenius.com/docs/4aa5-7619.pdf Product Owner and Scrum Master is at least twofold: to assure software product quality and to facilitate the effectiveness of the team and the process. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

2. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

3. ASD relies on short feedback cycles as a way to provide flexibility and rapid adaptation to market fluctuations. In this context, decisions are also made more frequently. For instance, product releases and the related decisions take place in short intervals, instead of months/years as was the case with traditional software development approaches such as the waterfall model. Popular agile practices such as continuous integration [29] provide a tight connection to development to ensure errors are detected and fixed as soon as possible. The current tendency to shorten feedback cycles even further (e.g., continuously getting feedback from customers and being able to react on that) enhances the potential for software analytics. Continuous software engineering [30], which has its roots in ASD, represents a holistic approach to providing tight connections among all software development activities, including not only integration but also aspects such as business and development (BizDez) and development and operations (DevOps). (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 3)

4. Currently, in many software development companies, teams are using various specific tools (such as Jira, GitLab and SonarQube) in order to support the development process and the quality of the code and products. This is usually done in a regular retrospective meeting that involves all the team. As far as the code quality is concerned, those tools provide sufficient information for the Scrum Team. However, there is still a gap and the need for more solutions reflecting team effectiveness and process quality. It can be stated that, at present, process improvement activities are mainly based on developers' perceptions and little support is given to make process wise data-driven decisions. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

5. TABLE 1. Examples of actions to improve software quality for the adalah tabel yang menyajikan contoh tindakan untuk meningkatkan kualitas perangkat lunak dengan menggunakan alat analitik perangkat lunak. Tabel ini terdiri dari 38 baris dan memiliki 8 kolom.

Tabel tersebut menjelaskan beberapa indikator strategis yang digunakan untuk mengevaluasi kinerja perangkat lunak, seperti "Blocking" yang merupakan indikator strategis untuk mengidentifikasi potensi masalah dalam proses pengembangan. Dalam tabel ini juga dapat dilihat bahwa ada empat faktor utama yang digunakan untuk menilai kualitas perangkat lunak: Code Smells, Design Issues, Performance, dan Security.

Salah satu contoh kasus yang disajikan dalam tabel adalah "Blocking" files problem yang dialami oleh perusahaan NeverLate. Dalam kasus ini, analis perangkat lunak dapat menggunakan alat analitik untuk mengidentifikasi klas-klas file yang memiliki kualitas rendah dan membutuhkan perbaikan.

Analisis dari tabel menunjukkan bahwa perusahaan yang menggunakan Q-Rapids dapat meningkatkan kualitas perangkat lunak mereka dengan menggunakan data historis dan visualisasi data. Dengan demikian, mereka dapat mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Dalam kesimpulan, tabel ini menunjukkan bahwa penggunaan alat analitik perangkat lunak dapat membantu meningkatkan kualitas perangkat lunak dengan cara yang lebih objektif dan data-driven. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 6)

6. Currently, in many software development companies and software houses, teams are already using some common tools (such as Jira, GitLab, and SonarQube) to manage the development process and the quality of their code and products. Such tools are now embedded into developers' way of working, and into the processes used in companies. Therefore, when introducing the Q-Rapids tool, it has to be clear when it is going to be used to assess and improve software quality, e.g., before checking the status of the project in GitLab or Jira or afterwards. It needs to be clarified when exactly in the agile (or any other) process this new tool should be used. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 15)

7. Currently, in many software development companies and software houses, teams are already using some common tools (such as Jira, GitLab, and SonarQube) to manage the development process and the quality of their code and products. Such tools are now embedded into developers' way of working, and into the processes used in companies. Therefore, when introducing the Q-Rapids tool, it has to be clear when it is going to be used to assess and improve software quality, e.g., before checking the status of the project in GitLab or Jira or afterwards. It needs to be clarified when exactly in the agile (or any other) process this new tool should be used. (Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study, page 15)

8. Two well-accepted strategies that software companies can implement to preserve their competitive advantage, reducing their time to market, are Agile Software Development (ASD) and Reuse-Driven Software Engineering (RDSE) [1]. While ASD achieves this by having short validation cycles, incremental delivery and minimizing activities not directly related to executable code, RDSE reduces the effort necessary to pro-The associate editor coordinating the review of this manuscript and approving it for publication was Adnan Abid. duce artifacts by reusing existent knowledge (i.e., artifacts) such as source code, requirements, and test cases. (Enabling the Reuse of Software Development Assets Through a Taxonomy for User Stories, page 1)

### response

Agile software development dapat membantu meningkatkan software quality dengan cara berikut:

• Menggunakan short feedback cycles untuk mendapatkan umpan balik yang cepat dan efektif
• Melakukan perubahan secara terus-menerus dan iteratif untuk memastikan bahwa sistem yang dikembangkan sesuai dengan kebutuhan pelanggan
• Meningkatkan kerja sama antara tim pengembangan dan pelanggan melalui komunikasi yang lebih baik
• Menggunakan alat analitik perangkat lunak untuk mengidentifikasi masalah-masalah yang signifikan dan mengambil tindakan untuk memperbaiki kinerja perangkat lunak.

Referensi:
[Continuously Assessing and Improving Software Quality With Software Analytics Tools: A Case Study]
[Measuring and Improving Agile Processes in a Small-Size Software Development Company]

### reference


---

## Sample 19

- conversation_id: 13
- user_chat_id: 517
- bot_chat_id: 518

### user_input

Bagaimana machine learning dapat digunakan untuk memprediksi software quality?

### retrieved_context

1. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. The prediction of refactoring refers to identifying the locations (i.e., classes, methods) in the software system that need to be refactored. Machine learning (ML) techniques have been used to detect code smells and predict refactoring. Ratzinger et al. [39] conducted an empirical study on two open-source software projects to identify where refactoring can be applied. They used classification algorithms (J482, LMT, Rip, and NNge) to predict where in the code should be refactored based on the project development history obtained from the Concurrent Versions System (CVS). Al Dallal [40] carried out an empirical study to predict the opportunities of using the Move Method refactoring technique in the classes. Logistic regression models were applied to create the prediction models on seven open-source projects of different sizes (one large-scale project and the others were medium and small projects). (Revisiting Scenarios of Using Refactoring Techniques to Improve Software Systems Quality, page 1)

4. Software fault prediction process typically involves two phases which are denoted as training phase and the second is prediction phase where in the first phase, a model for prediction is constructed, which utilizes method or class level metrics of software with fault information associated with every single module of the software. Later, the same model is used to predict faulty classes in a new version of the software. SFP is effective to enhance the quality of software along with reducing the cost of testing. Also, it assists testing teams to limit testing on faulty classes only. Fault prediction in software possibly lays down yardstick for knowing, which areas may require attention. Many software fault prediction methods have been utilized [29], which contribute to three main elements [30]; Set of features, Label of Class, and finally the Model. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 3)

5. The prediction of software faults is the subject of several studies. Many techniques have been proposed for predicting a software fault, including Statistical and Machine Learning methods. These are described as:

Statistical methods are used to find a clear mathematical formula that absolutely identifies how classification should be performed. Kapila and Singh [85] used two statistical approaches to carry out his study: Logistic Regression and Univariate Binary Logistic Regression (UBR) which are useful for analysis of data with binary variables. In Bayesian inference [85], the design of the model relates the metrics with the content of software faults and the tendency of faults. The regression analysis is extensively utilized for prediction of bad smell in the code and linear regression in a case where only two classes of the dependent variable exist. The Multilayer Perceptron (MLP) is utilized to control faulty classes and the Radial Base functions are used to classify the faults according to the different categories of faults [87]. Xing et al. defines the significance of the model of Support Vector Machine (SVM). The SVM model can be used for small amount of data. SVM delivers greater Accuracy as compare to other techniques for predicting quality of software, but the performance of SVM is low in public datasets [86]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 4)

6. Object-oriented metrics have been empirically validated to predict design flaws. Large and complex software systems are usually faulty [11]. It is difficult to keep them away from faults or to decrease risk of faults in upcoming version. According to [75], focus of verification and verification activities is to classify and remove high-risk problems in software. In order to avoid or squeeze faults, quality control models for example fault-prone models can be used for prediction of classes likely to be faulty. In order to attain these objectives, several researchers studied faults in software and constructed fault-proneness models base, on the event of failure [10], [34], [47], [76], [77]. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

8. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

### response

Berikut beberapa cara machine learning dapat digunakan untuk memprediksi software quality:

* Menggunakan metode pengajaran mesin, seperti Support Vector Machines (SVM), Naive Bayes (NB), Decision Trees, dan Neural Networks, untuk membangun model prediksi berdasarkan data metric software.
* Menganalisis data fault dari proyek-software yang serupa atau versi sebelumnya untuk mengembangkan model prediksi.
* Menggunakan teknik machine learning, seperti Logistic Regression dan Univariate Binary Logistic Regression (UBR), untuk menganalisis data dengan variabel binary.
* Menggunakan teknik neural network, seperti Multilayer Perceptron (MLP) dan Radial Base functions, untuk klasifikasi fault berdasarkan kategori-kategori fault yang berbeda.

### reference


---

## Sample 20

- conversation_id: 13
- user_chat_id: 519
- bot_chat_id: 520

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

Machine Learning adalah teknik pembelajaran mesin (machine learning) yang digunakan dalam pengembangan perangkat lunak untuk mendeteksi kelemahan atau kesalahan dalam kode program.

### reference


---

## Sample 21

- conversation_id: 13
- user_chat_id: 521
- bot_chat_id: 522

### user_input

Mengapa machine learning banyak digunakan?

### retrieved_context

1. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. TABLE 2. Electronic database.

Dalam penelitian ini, ditemukan beberapa pola penting dalam penggunaan teknik kecerdasan buatan (Artificial Intelligence) di bidang rekayasa perangkat lunak. Analisis yang dilakukan menunjukkan bahwa pembelajaran mesin (Machine Learning) adalah teknik AI yang paling umum digunakan.

Data menunjukkan bahwa ML telah digunakan secara luas dalam berbagai fase pengembangan perangkat lunak, termasuk fase analitik desain dan data persiapan. Hal ini menunjukkan bahwa ML dapat membantu mendukung aktivitas-aktivitas yang kompleks dan menghabiskan sumber daya.

Dalam fase pengujian, juga ditemukan bahwa ML digunakan secara luas untuk melakukan automasi tes perangkat lunak, sehingga membantu meningkatkan efisiensi dalam pengembangan perangkat lunak. Pada fase analitik desain dan data persiapan, ML juga menunjukkan kemampuan yang baik dalam mendukung aktivitas-aktivitas.

Dari analisis ini dapat disimpulkan bahwa AI telah menjadi bagian penting dalam rekayasa perangkat lunak modern. Penggunaan AI, terutama pembelajaran mesin, telah meningkatkan efisiensi dan produktivitas dalam pengembangan perangkat lunak. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 5)

4. Statistical methods are reflected as black-box solutions since these are extremely dependent on data, it is encouraging to perceive that more researchers are discovering the capability of machine learning methods to predict fault-prone modules.

TABLE 9. Data usage by studies. The literature review revealed that 59% used machine learning, and 22% used statistical methods [21]. Different machine learning methods and performance measures are examined which use object-oriented metrics for fault prediction. These are grouped into tables where studies from 1990-2003

TABLE 10. Datasets used by studies. are depicted in Table 11, studies in between 2004-2007 in Table 12 and studies between 2008-2020 mentioned in Table 13 [7], [94]- [104]. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

5. Organizational and team-based factors (OTBF) is regarded as ''the key factor in predicting the acceptance of several technologies and systems'' [47]. In the context of SE, research indicated that OTBF has a positive effect on metamodeling acceptance [47] and model-driven engineering [67], [68].

In this study, it is posited that if the organization provides sufficient support and training for SBSET, there is a great chance that the end-users' acceptance of SBSET will be increased. Thus, the following is hypothesized: H9: OTBF has a positive effect on SBSET acceptance. (The Acceptance of Search-Based Software Engineering Techniques: An Empirical Evaluation Using the Technology Acceptance Model, page 1)

6. Artificial Intelligence (AI) has rapidly emerged as one of the most prominent areas of research and development in recent years [1], [2]. AI systems are increasingly being integrated into our daily lives, playing a vital role in various applications spanning healthcare, finance, transportation, education, and entertainment [3], [4]. As an example, ChatGPT had around 1 million users within 5 days of its availability [1]. As AI systems become more ubiquitous, ensuring their high quality is crucial, as even minor flaws in AI software can lead to significant consequences [5]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 1)

7. In order to facilitate requirements traceability, researchers have suggested that devising a feedback mechanism, such as adding user feedback during the model training process in order to improve feature selection and performance, can really help the cause of generalizability. One of such works is presented by Sultanov et al. [3], which provides a very good basis for further developments.

In order to improve prediction accuracy and better reliability of results, more experiments using larger numbers of datasets and software applications have also been suggested [99], [115], [188], [237].

Researchers in the articles have also suggested investigating further regarding the suitable metrics and loss functions employed in the evaluation of ML for SE-focused techniques, especially for multi-class classification problems [125].

Future research directions also include automata learning for emergent middle-wares and using ML to address complex system integration problems, especially in system of systems such as the internet of things. Moreover, researchers are encouraged to devise adaptable, easily integrable, and scalable solutions in the area. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 13)

8. With the rapid development of information technology, the scale of data appears explosive growth. Mining valuable information from complex data has great practical significance [1]. As an important method in the field of data mining, clustering algorithm is widely used in data analysis and mining. DBSCAN algorithm is a typical clustering algorithm, and data density is as a measure, which can identify arbitrary shape classes and noise points of data sets. Some data show that by 2020, the data accumulated by China will account for 20% of the global data. Nowadays, both the government and enterprises have accumulated a large amount of data [2], and mining useful information from these data has great research value. As an important technology in the field of data mining, clustering has been applied in many fields, such as pattern recognition, information retrieval, network public opinion prediction and so on. (DBSCAN-Based Automatic De-Duplication for Software Quality Inspection Data, page 1)

### response

Pembelajaran Mesin (Machine Learning) seringkali digunakan karena algoritmanya yang dapat mereplikasi perilaku manusia. Selain itu, ML juga dapat membantu dalam aktivitas-aktivitas kompleks dan menghabiskan sumber daya, seperti fase analitik desain dan data persiapan di pengembangan perangkat lunak.

(Sumber: A Literature Review of Using Machine Learning in Software Development Life Cycle Stages)

Saya tidak menemukan informasi lebih lanjut tentang alasan lain mengapa machine learning banyak digunakan.

### reference


---

## Sample 22

- conversation_id: 13
- user_chat_id: 523
- bot_chat_id: 524

### user_input

Apa manfaat machine learning dalam software development?

### retrieved_context

1. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing. The study highlights the use of ML techniques in various software testing activities such as testcase generation and oracle construction. Results of the study show that a vast majority of articles employ supervised learning, such as ANN and DT, to solve testing-related problems. Moreover, the key advantages and disadvantages of using ML for software testing are discussed. Mainly, the advantage of ML techniques is their scalability and efficient application to large-scale and complex software systems. The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

4. The software engineering community is rapidly adopting machine learning for transitioning modern-day software towards highly intelligent and self-learning systems. However, the software engineering community is still discovering new ways how machine learning can offer help for various software development life cycle stages. In this article, we present a study on the use of machine learning across various software development life cycle stages. The overall aim of this article is to investigate the relationship between software development life cycle stages, and machine learning tools, techniques, and types. We attempt a holistic investigation in part to answer the question of whether machine learning favors certain stages and/or certain techniques. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

5. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

6. In the requirements stage, writing requirements specifications is highly deemed to be a human-centric task. Prior work by Pandita et al. [50] and Jahan et al. [51] have inferred the most probable specifications and identified its unexpected behaviors from various artifacts by employing ML techniques, respectively. Ferrari et al. [52] identified ambiguous requirements among different domains using ML. In the architecture and design stage, predicting design patterns is an important reverse engineering activity to improve software integrity. However, it often suffers from false positives and negatives [53]. As the number of patterns is increasing rapidly due to their variations, the process of recognizing these patterns can be effectively learned using ML [53]. In the implementation stage, detecting code smells in a large codebase can be extremely difficult for a human as opposed to a machine, thus ML techniques can greatly reduce this effort of detecting code smells or technical debt [30], [31]. In quality assurance, there is a need to ensure that the system remains error-free or to be able to timely identify the cause of failure. ML techniques employed in literature for this purpose proved to be promising in detecting software faults [34]- [36]. Test generation is also considered to be a task that requires human intelligence. Zhang et al. [54] have employed ML to automatically generate test data in order to improve return on investment. In software maintenance, Malgonde et al. [55] have shown ML techniques perform significantly better at predicting the effort as compared to the team estimates (human-centric). (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

7. On the other hand, AI shows a positive impact on efficiency (estimate = 0.7557, p = 0.021), where machine learning algorithms assist in tasks such as pattern recognition and design optimization, leading to reduced design time and enhanced resource management. AI accelerates prototyping via ML-driven pattern recognition (e.g., NSGA-III for modularization [38]), though at the cost of architectural rigor. These findings indicate that AI can improve operational flow in design. However, its impact on quality remains an area for potential development. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 8)

8. As software products become pervasive in all areas of society, the productive building of high-quality software has become crucial to the software industry. The rise of artificial intelligence (AI) applications is potentially a game-changer in improving Software Engineering (SE) phases to ensure higher-quality software, accelerate productivity, and increase project success rates. AI has the capability to assist software teams in many aspects, from automating certain activities in an SE phase to providing project analytics and actionable recommendations, and even making decisions [1]. AI techniques can support software engineers by detecting parts of the SE phases that are more likely to contain vulnerabilities and raising alerts about these issues. Such techniques can help to prioritize efforts and optimize inspection and testing costs. They (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 1)

### response

Berdasarkan konteks yang diberikan, beberapa manfaat machine learning dalam software development adalah:

* Scalability dan efisiensi aplikasi pada skala besar dan kompleks
* Mampu mengidentifikasi kekurangan data yang sesuai dengan proses belajar
* Dapat mendeteksi keamanan (security) di dalam sistem software
* Bisa membantu merancang prototipe GUI
* Bisa melakukan re-modularisasi software untuk meningkatkan konsistensi dan efisiensi sumber daya
* Bisa mendeteksi code smells atau teknologi utang yang tidak terdeteksi oleh manusia

### reference


---

## Sample 23

- conversation_id: 13
- user_chat_id: 525
- bot_chat_id: 526

### user_input

Bagaimana machine learning berbeda dari deep learning?

### retrieved_context

1. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Statistical methods are reflected as black-box solutions since these are extremely dependent on data, it is encouraging to perceive that more researchers are discovering the capability of machine learning methods to predict fault-prone modules.

TABLE 9. Data usage by studies. The literature review revealed that 59% used machine learning, and 22% used statistical methods [21]. Different machine learning methods and performance measures are examined which use object-oriented metrics for fault prediction. These are grouped into tables where studies from 1990-2003

TABLE 10. Datasets used by studies. are depicted in Table 11, studies in between 2004-2007 in Table 12 and studies between 2008-2020 mentioned in Table 13 [7], [94]- [104]. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. TABLE 1. Classification by articles.

Dalam penelitian ini, terdapat beberapa jenis teknik pembelajaran mesin (machine learning) yang digunakan dalam siklus hidup perangkat lunak. Berdasarkan analisis artikel-artikel yang dipilih, dapat dilihat bahwa sekitar 73% dari total artikel (193/263) menggunakan teknik supervised learning untuk mendeteksi kelemahan atau kesalahan dalam kode program.

Dalam supervised learning, model dibuat dengan melibatkan dataset yang telah terlabel. Model ini kemudian digunakan untuk mengklasifikasikan data baru menjadi kategori "Buggy" (kesalahan) atau "Correct" (benar). Sementara itu, sekitar 6% dari artikel-artikel tersebut menggunakan teknik unsupervised learning, di mana model dibuat tanpa melibatkan dataset yang telah terlabel.

Selain itu, juga ditemukan bahwa sekitar 2% dari total artikel (4/263) menggunakan teknik semi-supervised learning dan sekitar 0.4% menggunakan reinforcement learning, serta 17% menggunakan analytical learning. Pada umumnya, metode klasifikasi yang paling banyak digunakan adalah ANN (Artificial Neural Network), diikuti oleh RF (Random Forest), DT (Decision Tree), dan NB (Naïve Bayes).

Dari data ini dapat disimpulkan bahwa artikel-artikel tersebut berfokus pada penggunaan teknik pembelajaran mesin untuk mendeteksi kelemahan dalam kode program, serta perbandingan antara berbagai metode klasifikasi. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8)

5. TABLE 3. (Continued.) Articles by ML techniques.

Dalam penelitian ini, beberapa teknik Machine Learning (ML) digunakan dalam berbagai tahapan siklus pengembangan perangkat lunak. Hasil survei menunjukkan bahwa metode klasifikasi paling banyak digunakan dalam proses analisis data. Dari 10 artikel yang dianalisis, terdapat empat artikel yang menggunakan teknik klasifikasi untuk memprediksi perilaku pengguna dan kinerja sistem.

Satu artikel lainnya menggunakan teknik rekomendasi untuk memberikan saran kepada pengembang perangkat lunak dalam memilih teknologi yang sesuai. Dari analisis ini, dapat disimpulkan bahwa peneliti menggunakan berbagai jenis ML untuk meningkatkan efisiensi dan kualitas dalam proses pengembangan perangkat lunak.

Namun demikian, terdapat beberapa kelemahan dalam penelitian ini. Salah satu masalahnya adalah kompleksitas data yang digunakan sebagai input untuk model ML. Hal ini menyebabkan kesulitan dalam mendapatkan hasil akurasi yang tinggi. Oleh karena itu, diperlukan perhatian lebih dalam hal pengumpulan dan proses pengolahan data.

Dalam penelitian ini, analisis kualitas juga menjadi perhatian utama. Dua artikel di antaranya menggunakan teknik klasifikasi untuk menganalisis perilaku pengguna dan memberikan rekomendasi kepada pengembang perangkat lunak. Dari hasil survei yang dilakukan, dapat disimpulkan bahwa peneliti menggunakan berbagai jenis ML dalam proses pengembangan perangkat lunak.

Masalah lainnya adalah adanya kekurangan data yang memadai untuk digunakan sebagai input model ML. Hal ini menyebabkan sulitnya mendapatkan hasil akurasi yang tinggi. Oleh karena itu, diperlukan perhatian lebih dalam hal pengumpulan dan proses pengolahan data.

Selain itu, juga ditemukan bahwa peneliti menggunakan teknik rekomendasi untuk memberikan saran kepada pengembang perangkat lunak dalam memilih teknologi yang sesuai. Dari analisis ini dapat disimpulkan bahwa penelitian tersebut berfokus pada penerapan ML dalam meningkatkan efisiensi dan kualitas proses pengembangan perangkat lunak.

Dalam keseluruhan, hasil survei menunjukkan bahwa peneliti menggunakan beberapa jenis teknik ML untuk memenuhi kebutuhan pengembangan perangkat lunak. Namun demikian, masih terdapat kelemahan dalam penelitian ini yang perlu diperhatikan dan ditangani dengan lebih baik di masa depan. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 17)

6. By the type of ML, we mean how the models have been trained, i.e., supervised, semi-supervised, unsupervised, reinforcement, or analytical learning. Supervised learning is based on a training set and a test set taken from the dataset. The model training is done by taking multiple labeled samples from the train set. After the model is trained, its performance is evaluated using the test set. In semi-supervised learning, both labeled and unlabelled data are employed in order to train the model. The dataset is divided into unsupervised clusters as such. Then, the class information is obtained by learning the clustering outcomes [216]. Unsupervised learning requires no training dataset. For instance, in unsupervised learning for fault detection, software instances are usually grouped into clusters and each cluster is labeled as ''Buggy'' or ''Correct''. However, each cluster needs to be labeled manually by the individuals with expertise [198]. Reinforcement learning refers to unsupervised goal-oriented learning performed by an agent directly interacting with the environment. Analytical learning is aimed at generating solutions based on background knowledge and improving inference iteratively [253]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 8)

7. AI-based machine learning requires a huge number of inputs as the knowledge and different intelligent algorithms in order to make the right decision. By looking at an example using technology in unmanned vehicles, there will be a basic understanding of how machine learning or machine intelligence work. The development of machine intelligence is still far from mimicking the cognitive competence of the human brain. It is still challenging to deal with those data effectively and making a driving decision accurately and quickly [17]. Machine learning sometimes returns an inaccurate prediction based on the collection of training data and an engineer needs to make some adjustments to avoid significant losses in terms of public safety. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

8. The prediction of refactoring refers to identifying the locations (i.e., classes, methods) in the software system that need to be refactored. Machine learning (ML) techniques have been used to detect code smells and predict refactoring. Ratzinger et al. [39] conducted an empirical study on two open-source software projects to identify where refactoring can be applied. They used classification algorithms (J482, LMT, Rip, and NNge) to predict where in the code should be refactored based on the project development history obtained from the Concurrent Versions System (CVS). Al Dallal [40] carried out an empirical study to predict the opportunities of using the Move Method refactoring technique in the classes. Logistic regression models were applied to create the prediction models on seven open-source projects of different sizes (one large-scale project and the others were medium and small projects). (Revisiting Scenarios of Using Refactoring Techniques to Improve Software Systems Quality, page 1)

### response

Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 24

- conversation_id: 13
- user_chat_id: 527
- bot_chat_id: 528

### user_input

Apa contoh penggunaan machine learning dalam software engineering?

### retrieved_context

1. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Many types of research in the past have applied ML to software architecture and design. The applications include design models, which are comprised of recommendation models for software processes/services. Apart from this, model smells and refactoring techniques of object-oriented structures using ML have also been proposed in the articles. White et al. [26] introduced DL to software language modeling based on information retrieval models. Design pattern prediction primarily focuses on recognizing design patterns in software through source code or user interface layout using ML techniques. For example, Nguyen et al. [27] proposed an approach known as DeepUI in order to semi-automate the design tasks by learning from previous UI design patterns. Development effort estimation refers to estimating effort for the development of software projects using ML techniques. Ionescu [28] used ANN to automate effort estimation by learning from textual features of project tasks. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 6)

4. Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing. The study highlights the use of ML techniques in various software testing activities such as testcase generation and oracle construction. Results of the study show that a vast majority of articles employ supervised learning, such as ANN and DT, to solve testing-related problems. Moreover, the key advantages and disadvantages of using ML for software testing are discussed. Mainly, the advantage of ML techniques is their scalability and efficient application to large-scale and complex software systems. The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

5. TABLE 2. Electronic database.

Dalam penelitian ini, ditemukan beberapa pola penting dalam penggunaan teknik kecerdasan buatan (Artificial Intelligence) di bidang rekayasa perangkat lunak. Analisis yang dilakukan menunjukkan bahwa pembelajaran mesin (Machine Learning) adalah teknik AI yang paling umum digunakan.

Data menunjukkan bahwa ML telah digunakan secara luas dalam berbagai fase pengembangan perangkat lunak, termasuk fase analitik desain dan data persiapan. Hal ini menunjukkan bahwa ML dapat membantu mendukung aktivitas-aktivitas yang kompleks dan menghabiskan sumber daya.

Dalam fase pengujian, juga ditemukan bahwa ML digunakan secara luas untuk melakukan automasi tes perangkat lunak, sehingga membantu meningkatkan efisiensi dalam pengembangan perangkat lunak. Pada fase analitik desain dan data persiapan, ML juga menunjukkan kemampuan yang baik dalam mendukung aktivitas-aktivitas.

Dari analisis ini dapat disimpulkan bahwa AI telah menjadi bagian penting dalam rekayasa perangkat lunak modern. Penggunaan AI, terutama pembelajaran mesin, telah meningkatkan efisiensi dan produktivitas dalam pengembangan perangkat lunak. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 5)

6. TABLE 6. Application, improvement and development of artificial intelligence techniques in the primary studies. TABLE 6. Aplikasi, peningkatan, dan pengembangan teknik kecerdasan buatan dalam studi primer menunjukkan berbagai cara peneliti telah menggunakan teknik kecerdasan buatan dalam software engineering. Terdapat beberapa pola yang dapat dilihat dari data ini.

Kolom "Technique" menampilkan variasi teknik kecerdasan buatan, seperti Machine Learning (ML), Natural Language Processing (NLP), dan Hybrid ML. Keterlibatan ML sangat menonjol dalam studi-studi tersebut, baik secara individu maupun kombinasi dengan teknik lain.

Dari "Application", dapat dilihat bahwa peneliti telah menggunakan AI untuk berbagai tujuan, termasuk prediksi kegagalan software, klasifikasi permintaan pengguna, analisis data besar, dan lain-lain. Penekanan pada pengembangan model yang didorong oleh data tampaknya menjadi fokus utama banyak peneliti.

"Improvement and Development" menunjukkan bahwa AI tidak hanya digunakan untuk aplikasi tetapi juga untuk meningkatkan kemampuan beberapa teknik dalam software engineering, seperti perbaikan akurasi prediksi risiko keamanan dan pengembangan model yang lebih maju. Kegunaan dari kombinasi antara Machine Learning dengan Neural Network (ANN) tampaknya menjadi bidang penelitian penting.

Pada "Primary Studies", variasi jenis studi yang menggunakan AI dalam software engineering dapat dilihat, seperti penggunaan model data didorong untuk analisis sistem, penelitian pada kemampuan AI dalam memprediksi kegagalan, dan pengembangan model yang lebih akurat dengan bantuan dari teknik kombinasi ML.

Dalam keseluruhan, tabel ini menunjukkan bahwa peneliti telah mengembangkan berbagai aplikasi dan teknologi yang menggunakan kecerdasan buatan dalam software engineering. Penggunaan AI telah diterapkan untuk meningkatkan akurasi prediksi, memperbaiki kemampuan klasifikasi, serta pengembangan model yang lebih maju dengan bantuan dari kombinasi teknik-teknik yang berbeda-beda.

Penggunaan kecerdasan buatan secara luas dalam beberapa bidang termasuk software engineering menunjukkan bahwa teknologi ini memiliki potensi besar untuk meningkatkan kinerja, memperbaiki akurasi analisis data, dan mengembangkan model yang lebih akurat. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 9)

7. The software engineering community is rapidly adopting machine learning for transitioning modern-day software towards highly intelligent and self-learning systems. However, the software engineering community is still discovering new ways how machine learning can offer help for various software development life cycle stages. In this article, we present a study on the use of machine learning across various software development life cycle stages. The overall aim of this article is to investigate the relationship between software development life cycle stages, and machine learning tools, techniques, and types. We attempt a holistic investigation in part to answer the question of whether machine learning favors certain stages and/or certain techniques. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

8. The literature review reveals that experimental studies used statistical, and machine learning models for their experiments. Machine learning models have widely used a comparison to statistical methods in the context of SFP. Recent studies show the use of Support Vector Machine, Naive Bayes, Decision Tree, and ANN models for fault prediction. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 17)

### response

Beberapa contoh penggunaan machine learning dalam software engineering adalah:

* Pembelajaran mesin (Machine Learning) telah digunakan secara luas dalam berbagai fase pengembangan perangkat lunak, termasuk fase analitik desain dan data persiapan.
* ML telah digunakan untuk melakukan automasi tes perangkat lunak, sehingga membantu meningkatkan efisiensi dalam pengembangan perangkat lunak.
* Machine learning telah digunakan untuk berbagai tujuan, termasuk prediksi kegagalan software, klasifikasi permintaan pengguna, analisis data besar, dan lain-lain.
* AI telah digunakan untuk meningkatkan kemampuan beberapa teknik dalam software engineering, seperti perbaikan akurasi prediksi risiko keamanan dan pengembangan model yang lebih maju.

Informasi tersebut didapatkan dari berbagai sumber yang disebutkan di dalam konteks.

### reference


---

## Sample 25

- conversation_id: 13
- user_chat_id: 529
- bot_chat_id: 530

### user_input

Bagaimana machine learning dapat membantu software testing?

### retrieved_context

1. Some studies, e.g., [8], [10]- [12], have already analyzed the application of ML in SE in the past. Durelli et al. [8] conducts a systematic mapping study on the application of ML for software testing. The study highlights the use of ML techniques in various software testing activities such as testcase generation and oracle construction. Results of the study show that a vast majority of articles employ supervised learning, such as ANN and DT, to solve testing-related problems. Moreover, the key advantages and disadvantages of using ML for software testing are discussed. Mainly, the advantage of ML techniques is their scalability and efficient application to large-scale and complex software systems. The disadvantage, on the other hand, is the unavailability of data that fits well with the learning process. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

2. Although there are many successful studies about the automated generation of test cases, determining whether a program has passed a given test remains largely manual. Langdon et al. [16] proposed the use of search-based learning from existing open-source test suites to automatically generate partially correct test oracles. They argued that mutation testing, n-version computing, and machine learning could be combined to allow automated output checking to catch up with progress on automated input generation.

AI software testing differs from AI-based software testing in diverse views such as test objectives, test focuses, test scope, test coverage as well as test techniques and tools. For example, AI-based testing primarily aims to increase efficiency for a test process, reduce testing costs by reduce human operations, and increase bug detection effectiveness and speed. AI testing aims to provide on-demand testing services for AI software to support software validation and quality engineering process. AI-based testing majorly focuses on test selection, automatic test execution, bug detection and prediction based large-scale testing history data and AI techniques. In addition, AI testing needs innovative continuous, timeliness, and currency testing techniques. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

3. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

4. TABLE 2. Electronic database.

Dalam penelitian ini, ditemukan beberapa pola penting dalam penggunaan teknik kecerdasan buatan (Artificial Intelligence) di bidang rekayasa perangkat lunak. Analisis yang dilakukan menunjukkan bahwa pembelajaran mesin (Machine Learning) adalah teknik AI yang paling umum digunakan.

Data menunjukkan bahwa ML telah digunakan secara luas dalam berbagai fase pengembangan perangkat lunak, termasuk fase analitik desain dan data persiapan. Hal ini menunjukkan bahwa ML dapat membantu mendukung aktivitas-aktivitas yang kompleks dan menghabiskan sumber daya.

Dalam fase pengujian, juga ditemukan bahwa ML digunakan secara luas untuk melakukan automasi tes perangkat lunak, sehingga membantu meningkatkan efisiensi dalam pengembangan perangkat lunak. Pada fase analitik desain dan data persiapan, ML juga menunjukkan kemampuan yang baik dalam mendukung aktivitas-aktivitas.

Dari analisis ini dapat disimpulkan bahwa AI telah menjadi bagian penting dalam rekayasa perangkat lunak modern. Penggunaan AI, terutama pembelajaran mesin, telah meningkatkan efisiensi dan produktivitas dalam pengembangan perangkat lunak. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 5)

5. The software engineering (SE) community is continuously looking for better and more efficient ways of building high-quality software systems. However, in practice, the strong emphasis on time to market tends to ignore many, well-known SE recommendations. That is, practitioners focus more on programming as compared to requirements gathering, planning, specification, architecture, design, and documentation -all of which are ultimately known to greatly benefit the cost-effectiveness and quality of software systems. Lack of human resources is often cited as the main reason for doing so. Herein lies the great potential for machine learning (ML) since its algorithms are proven to be most befitting to problem domains that aim to replicate human behavior. Hence, it stands to reason that human-centric SE activities should also benefit from ML [1]. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

6. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

7. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

8. In the requirements stage, writing requirements specifications is highly deemed to be a human-centric task. Prior work by Pandita et al. [50] and Jahan et al. [51] have inferred the most probable specifications and identified its unexpected behaviors from various artifacts by employing ML techniques, respectively. Ferrari et al. [52] identified ambiguous requirements among different domains using ML. In the architecture and design stage, predicting design patterns is an important reverse engineering activity to improve software integrity. However, it often suffers from false positives and negatives [53]. As the number of patterns is increasing rapidly due to their variations, the process of recognizing these patterns can be effectively learned using ML [53]. In the implementation stage, detecting code smells in a large codebase can be extremely difficult for a human as opposed to a machine, thus ML techniques can greatly reduce this effort of detecting code smells or technical debt [30], [31]. In quality assurance, there is a need to ensure that the system remains error-free or to be able to timely identify the cause of failure. ML techniques employed in literature for this purpose proved to be promising in detecting software faults [34]- [36]. Test generation is also considered to be a task that requires human intelligence. Zhang et al. [54] have employed ML to automatically generate test data in order to improve return on investment. In software maintenance, Malgonde et al. [55] have shown ML techniques perform significantly better at predicting the effort as compared to the team estimates (human-centric). (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 1)

### response

Machine learning dapat membantu software testing dengan:

* Membantu otomatisasi tes perangkat lunak
* Meningkatkan efisiensi dalam pengembangan perangkat lunak
* Mendukung aktivitas-aktivitas yang kompleks dan menghabiskan sumber daya.
* Menganalisis data untuk mendeteksi kesalahan atau kekurangan pada sistem perangkat lunak.
* Menggunakan teknik pembelajaran mesin (machine learning) untuk mengenali pola-pola dalam kode perangkat lunak dan mendeteksi potensi kesalahan.

Informasi tersebut ditemukan di dokumen "A Literature Review of Using Machine Learning in Software Development Life Cycle Stages" dan "Systematic Mapping: Artificial Intelligence Techniques in Software Engineering".

### reference


---

## Sample 26

- conversation_id: 13
- user_chat_id: 531
- bot_chat_id: 532

### user_input

Bagaimana machine learning digunakan untuk memprediksi software defects?

### retrieved_context

1. The faults are not uniformly dispersed within the software components. Some classes have a relatively high number of faults as compare to others and are clustered in a limited number of classes [6]. Source code quality is measured through internal metrics whereas the behavior or functionality of the software is measured by external metrics [4]. In general, these two types of metrics are utilized to assess the quality of the software to indicate the degree of reliability of the software. Presently in software engineering, numerous prediction approaches are being used in the research that includes prediction of reuse, prediction of testing effort, prediction of cost, prediction of security, prediction of faults, prediction of quality, and prediction of stress [7]. Out of these, software fault prediction is an emergent research domain where defective classes are identified during the initial phases of development project [8] by utilizing machine learning [9]. Many approaches make use of typical methods of machine learning, which consist of Support Vector Machines (SVM), Naive Bayes (NB) [10], Decision Trees [11], and Neural Networks [12]. In SFP, these techniques are exercised by using metric measurements, and the fault information obtained by similar software projects [13] or previous versions to construct models to predict faults. Suppose, by using metrics to build a model of fault prediction [14] for the calculation of inheritance of software, cohesion, coupling, size, and complexity. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

2. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Software Defects Prediction (SDP) consists in identifying defective software components, being considered an essential activity during software development. It represents the activity of identifying defective software modules in new versions of a software system [1]. SDP is considered of great importance in software engineering, as it contributes to continuously improving the software quality. Developing high quality software systems is expensive and, in this context, SDP is used for increasing the cost effectiveness of quality assurance and testing [2]. By detecting fault-prone modules in new versions of a software system, SDP helps to allocate the effort so as to test more thoroughly those modules [1]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

4. Fault prediction is topic of numerous researches studies. A number of methods are recommended for the prediction of software faults, which include machine learning, and Statistical methods. Both methods are explained in detail in subsequent lines. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 4)

5. The prediction of software faults is the subject of several studies. Many techniques have been proposed for predicting a software fault, including Statistical and Machine Learning methods. These are described as:

Statistical methods are used to find a clear mathematical formula that absolutely identifies how classification should be performed. Kapila and Singh [85] used two statistical approaches to carry out his study: Logistic Regression and Univariate Binary Logistic Regression (UBR) which are useful for analysis of data with binary variables. In Bayesian inference [85], the design of the model relates the metrics with the content of software faults and the tendency of faults. The regression analysis is extensively utilized for prediction of bad smell in the code and linear regression in a case where only two classes of the dependent variable exist. The Multilayer Perceptron (MLP) is utilized to control faulty classes and the Radial Base functions are used to classify the faults according to the different categories of faults [87]. Xing et al. defines the significance of the model of Support Vector Machine (SVM). The SVM model can be used for small amount of data. SVM delivers greater Accuracy as compare to other techniques for predicting quality of software, but the performance of SVM is low in public datasets [86]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 4)

6. Object-oriented metrics have been empirically validated to predict design flaws. Large and complex software systems are usually faulty [11]. It is difficult to keep them away from faults or to decrease risk of faults in upcoming version. According to [75], focus of verification and verification activities is to classify and remove high-risk problems in software. In order to avoid or squeeze faults, quality control models for example fault-prone models can be used for prediction of classes likely to be faulty. In order to attain these objectives, several researchers studied faults in software and constructed fault-proneness models base, on the event of failure [10], [34], [47], [76], [77]. Software prediction models are constructed using a variety of machine learning methods, such as Genetic Programming [78], Decision Trees [79], Neural Networks [80], Naive Bayes (NB) [21], Case-Based Reasoning [81], and Blurring Logic [82]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

8. Software fault prediction process typically involves two phases which are denoted as training phase and the second is prediction phase where in the first phase, a model for prediction is constructed, which utilizes method or class level metrics of software with fault information associated with every single module of the software. Later, the same model is used to predict faulty classes in a new version of the software. SFP is effective to enhance the quality of software along with reducing the cost of testing. Also, it assists testing teams to limit testing on faulty classes only. Fault prediction in software possibly lays down yardstick for knowing, which areas may require attention. Many software fault prediction methods have been utilized [29], which contribute to three main elements [30]; Set of features, Label of Class, and finally the Model. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 3)

### response

Machine learning digunakan dalam prediksi software defects dengan teknik-teknik seperti:

* Support Vector Machines (SVM)
* Naive Bayes (NB)
* Decision Trees
* Neural Networks
* Genetic Programming
* Case-Based Reasoning
* Blurring Logic

Teknik-teknik ini digunakan untuk membangun model yang dapat memprediksi kelas-kelas yang mungkin mengandung kerusakan software.

### reference


---

## Sample 27

- conversation_id: 13
- user_chat_id: 533
- bot_chat_id: 534

### user_input

Apa hubungan machine learning dengan CNN?

### retrieved_context

1. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

2. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

[39] TJ Bosch, T Hanna, KA Fercho, LA Baugh. Behavioral performance and visual strategies during skill acquisition using a novel tool use motor learning task. (2018-12)

[40] W Choi. The effect of task-oriented training on upper-limb function, visual perception, and activities of daily living in acute stroke patients: A pilot study. (2022-03)

[41] I Pysmennyi, R Kyslyi, A Petrenko. Edge computing in multi-scope service-oriented mobile healthcare systems. (2019-03)

[42] J Lv, Q Sun, Q Li, L Moreira-Matias. Multi-scale and multiscope convolutional neural networks for destination prediction of trajectories. (2020-08)

[43] AA Saputra, K Wada, S Masuda, N Kubota. Multi-scopic neuro-cognitive adaptation for legged locomotion robots. (2021-08)

[44] AF Zhu, P Rahgozar, KC Chung. Advances in proximal interphalangeal joint arthroplasty. (2018-05)

[45] J.-S Won, S Lee. Geometry-based finger kinematic models for joint rotation configuration and parameter estimation. (2020-07)

[46] AR A Besari, AA Saputra, WH Chin, N Kubota, Kurnianingsih. Feature-based egocentric grasp pose classification for expanding humanobject interactions. (2021-06)

[47] PB Shull, S Jiang, Y Zhu, X Zhu. Hand gesture recognition and finger angle estimation via wrist-worn modified barometric pressure sensing. (2019-04)

[48] I Imbinto, F Montagnani, M Bacchereti, C Cipriani, A Davalli, R Sacchetti, E Gruppioni, S Castellano, M Controzzi. The S-finger: A synergetic externally powered digit with tactile sensing and feedback. (2018-06)

[49] J Mazumder, LN Nahar, M Md Uddin Atique. Finger gesture detection and application using hue saturation value. (2018-08)

[50] WB Dou, WH Chin, N Kubota. Hand gesture communication using deep learning based on relevance theory,'. (2020-12)

[51] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[52] Y Cheng. Backpropagation for fully connected cascade networks. (2017-08)

[53] P Gajbhiye, N Mingchinda, W Chen, SC Mukhopadhyay, T Wilaiprasitporn, RK Tripathy. Wavelet domain optimized Savitzky-Golay filter for the removal of motion artifacts from EEG recordings. (2021)

[54] R Chen, M Wang, J.-H Chang. A study of the pinch performance and subjective satisfaction with chopsticks of different lengths. (2017)

[55] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[56] YJ R De Kloe, IT C Hooge, C Kemner, DC Niehorster, M Nyström, RS Hessels. Replacing eye trackers in ongoing studies: A comparison of eye-tracking data quality between the Tobii pro TX300 and the tobii pro spectrum. (2022-01)

[57] EP Larsen, JM Kolman, FN Masud, F Sasangohar. Ethical considerations when using a mobile eye tracker in a patient-facing area: Lessons from an intensive care unit observational protocol. (2020-11)

[58] DC Niehorster, T Santini, RS Hessels, IT C Hooge, E Kasneci, M Nyström. The impact of slippage on the data quality of head-worn eye trackers. (2020-06)

[59] C Chen, W Guo, C Ma, Y Yang, Z Wang, C Lin. SEMGbased continuous estimation of finger kinematics via large-scale temporal convolutional network. (2021-05)

[60] C Dai, X Hu. Finger joint angle estimation based on motoneuron discharge activities. (2020-03)

[61] H Eschmann, ME Héroux, JH Cheetham, S Potts, J Diong. Thumb and finger movement is reduced after stroke: An observational study. (2019-06)

[62] SN Emhardt, M Wermeskerken, K Scheiter, T Gog. Inferring task performance and confidence from displays of eye movements. (2020-11)

[63] X Fang, F Yu, G Yang, Y Qu. Regression analysis with differential privacy preserving. (2019)

[64] H Zhu, X You, S Liu. Multiple ant colony optimization based on Pearson correlation coefficient. (2019)

[65] L Ke, A Kamat, J Wang, T Bhattacharjee, C Mavrogiannis, SS Srinivasa. Telemanipulation with Chopsticks: Analyzing human factors in user demonstrations. (2022-06)

[66] A Murata, T Doi, W Kageyama, Karwowski. Development of an eye-gaze input system with high speed and accuracy through target prediction based on homing eye movements. (2021)

[67] B Banire, D Al-Thani, M Qaraqe, K Khowaja, B Mansoor. The effects of visual stimuli on attention in children with autism spectrum disorder: An eye-tracking study. (2020) (Finger Joint Angle Estimation With Visual Attention for Rehabilitation Support: A Case Study of the Chopsticks Manipulation Test, page 2)

3. Several studies have developed many CNN methods or convolutional neural networks for object prediction applications such as balls, humans, and others. CNN can also be used for object detection and position prediction in three-dimensional environments because of its ability to extract complex visual features from image data taken from the camera. The CNN method is able to process image data in two dimensions, such as applications for detecting the position of the ball in real-time for goalkeeper robots [4], [5], [25]. The CNN method is also used for several mobile robot-vision applications [26], [27] such as service robots or collaboration of several industrial robots [28], [29]. This research aims to build a combination of ZED camera devices with CNN methods that have been used in previous research to detect and predict the position of the ball in the goal area. This model scenario is to be able to reach all lighting conditions with a camera that has artificial intelligence features. The CNN model as an intelligence feature is added so that the system can predict the position of the ball with a ZED camera that has features that can overcome changes in light intensity levels. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 1)

4. FIGURE 9. CNN model training result.

Gambar ini menampilkan grafik hasil pelatihan model CNN (Convolutional Neural Network). Grafik ini terlihat seperti garis di atas yang menunjukkan proses pengembangan akurasi model CNN selama proses pelatihan. Pada awalnya, akurasi model cukup rendah, tetapi kemudian meningkat secara signifikan seiring dengan berjalannya waktu dan iterasi pelatihan.

Pada grafik tersebut terdapat beberapa titik tertentu yang menunjukkan peningkatan drastis dalam akurasi. Meskipun tidak ada angka spesifik yang dapat diidentifikasi, namun jelas bahwa model CNN telah berhasil meningkatkan akurasinya hingga mencapai nilai yang sangat tinggi.

Dari grafik ini kita dapat menyimpulkan bahwa proses pelatihan model CNN telah berjalan dengan efektif dan akurasi model meningkat secara signifikan. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

5. This research uses the ROS system because it has the ability to integrate camera sensors with artificial intelligence methods and several other combined sensors in the robot. Fig. 4 shows the basic communication system for accessing the ZED camera on the robot. Image information is acquired over time and processed in real-time.  The prediction system that has been created using the CNN algorithm tries to change the layer parameter model to get the best results in classifying the position of the predicted direction of the ball. The dataset was collected as shown in Fig. 6. The CNN design used is as in Fig. 7 and equations ( 4) to (9). Convolutional Neural Network (CNN) is a type of artificial neural network specifically designed to process two-dimensional grid-shaped data, such as images. The convolution layer, pooling layer, and fully connected layer are the three primary hierarchical layers of a CNN. The central component of a CNN is the convolution layer, where different visual elements like edges, textures, and patterns are detected by applying filters or kernels to the input. A feature map reflecting the position of a certain feature in the original image is produced by the convolution layer's filters scanning the entire input. The way that neurons in the human brain react to visual stimuli is comparable to this mechanism. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 4)

6. Qurishee [71] presented an autonomous pavement condition evaluation employing deep learning, an unmanned aerial vehicle (UAV), and Raspberry Pi tiny computer technologies, which improves road maintenance and renovation management efficiency and cost effectiveness. A lowcost Raspberry Pi smart defect-detecting camera was set up with the trained SSD MobileNet v1, which can be deployed with a UAV for real-time and remote pavement condition inspection. According to preliminary data, the smart pavement detector camera achieves 60% accuracy at 1.2 frames per second on the Raspberry Pi and 96% accuracy at 13.8 frames per second on a CPU-based computer. Hassan et al. [72] employs CNN models that are improved tiny YOLO V3 on UAVs and achieves good results, with precision, sensitivity, and F1 score values better than 85%, but without considering FPS. Sathvik et al. [39] introduce

TABLE 1. Comparison of object detection models deployed on edge device.

pothole detection, an edge computing framework that runs efficient deep neural networks, lowering the latency of earlier techniques. Using transfer learning-based models, an F1 score of 0.64. The YOLO V7 model had an F1 score of 0.51, which improved proportionally (the higher the F1 score, the more efficient the training model) as the number of epochs increased. The YOLO V7 runs on a CPU-based computer, however it does not consider run on edge devices.

Several studies using CNN models deployed on NVIDIA Jetson Nano devices include the SSD-MobileNet model with a batch size of 64 and mAP of 0.22 [48], the MobileNet V2 model, and the SSD Resnet50V1 model [34], [35]. The MobileNet V2 model using hyperparameter settings has a higher mAP of 0.0869 and average recall 0.241 than the SSD Resnet50V1. Yebes et al. [40] created a massive dataset of images with pothole annotations and road scenes from many cities across the world, captured with various cameras, vehicles, and viewpoints under varying environmental circumstances. Their fine-tuned Faster R-CNN Inception v2, Faster R-CNN Resnet101, and Faster R-CNN Inception-Resnet v2 models reached precision 75%, and their CNN model deployed the pothole detector on the Nvidia DrivePX2 platform running at 5-6 frames per second. Based on the findings of this investigation, CNN models were included in the hardware, as indicated in Table 1, although further research is needed to improve system performance (mAP, AR, F1 score) and speed up inference time. Based on previous studies on road damage, several researchers have utilized the CNN model by optimizing its network structure. Specifically, the YOLO model automates the network structure through the introduction of a new module. However, few YOLOv3 models incorporate hyperparameter optimization, with only one study utilizing the Bayesian method. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 1)

7. TABLE 1. The proposed system with related works.

Tabel ini menjelaskan sistem yang diusulkan bersama dengan karya terkait dalam penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang". Tabel ini berisi 39 baris dan 9 kolom, tetapi hanya memuat informasi singkat tentang beberapa studi terkait.

Variabel/kolom utama adalah:

* Judul penelitian yang berkaitan dengan metode CNN dan kamera Zed.
* Karya-karya yang relevan yang dikemukakan sebagai referensi.
* Deskripsi singkat tentang aplikasi robot penjaga gawang dan penggunaan metode CNN.

Nilai atau pola penting dari tabel ini adalah:

* Penggunaan metode CNN untuk mendeteksi posisi bola dalam lingkungan tiga dimensi, yang merupakan kemampuan utama dari metode tersebut.
* Aplikasi robot penjaga gawang sebagai salah satu penggunaan metode CNN.

Insight singkat yang bisa dibaca manusia adalah bahwa penelitian ini berusaha mengembangkan sistem kombinasi antara kamera Zed dan metode CNN untuk mendeteksi posisi bola dengan akurasi tinggi, serta memahami pergerakan bola dalam lingkungan yang beragam. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 3)

8. The pooling layer, which comes after the convolution layer, is meant to combine key information and lower the dimensionality of the feature map. Max pooling, which chooses the maximum value within each condensed area of the feature map, is a frequently used kind of pooling. This lessens the number of parameters that must be computed and increases the model's resistance to slight variations in the input features' locations.

CNNs typically have multiple sets of successive convolution and pooling layers, which allow the network to detect increasingly complex features at each layer. Early layers may detect simple edges and lines, while deeper layers may detect more complex objects, such as specific shapes and patterns.

The final input is supplied into the fully connected layer after passing through several convolution and pooling layers. Every neuron in this layer is connected to every other neuron in the layer before it, enabling the network to compile the features that were taken out of the earlier levels and come to a conclusion. An activation function that aids in the final classification, such as ReLU (Rectified Linear Unit) or Softmax, typically follows this completely connected layer.

This study designs and implements appropriate parameter values in each layer of the CNN used. Previous researchers have created several methods for artificial intelligence that have been tried to be implemented on the ERSOW robot. These methods are Label Propagation, Extra Tree Classifier, Ridge Classifier, Linear SVC, Passive Aggressive Classifier, AdaBoost, Label Spreading, Nearest Centroid, GaussianNB, and Dummy Classifier (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 5)

### response

Machine learning dan CNN (Convolutional Neural Network) memiliki hubungan yang erat. Dalam konteks penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang", CNN digunakan sebagai metode machine learning untuk mendeteksi posisi bola dalam lingkungan tiga dimensi.

CNN adalah jenis jaringan saraf tiruan yang dirancang khusus untuk memproses data berupa citra, seperti gambar dan video. Dalam penelitian ini, CNN digunakan untuk menganalisis citra dari kamera Zed untuk mendeteksi posisi bola dengan akurasi tinggi.

Dengan demikian, hubungan antara machine learning dan CNN adalah bahwa CNN adalah salah satu metode machine learning yang digunakan dalam penelitian ini untuk mendapatkan hasil yang baik.

### reference


---

## Sample 28

- conversation_id: 13
- user_chat_id: 535
- bot_chat_id: 536

### user_input

Bagaimana systematic literature review membantu membandingkan metode machine learning?

### retrieved_context

1. To present a comprehensive picture of quality for AI-based software, we conducted a systematic literature analysis following the approach by Kitchenham [14]. Systematic literature studies in software engineering can include reviews and syntheses of prior work, enabling researchers to gain an understanding of the state of a particular research subject. The findings of this SLR research should provide a more comprehensive picture of the gaps and support for software quality in the context of AI-based software systems. The following sections conduct key processes such as literature selection, string searches, and data extraction techniques in accordance with the guidelines of Peterson [15]. (Taxonomy of Quality Assessment for Intelligent Software Systems: A Systematic Literature Review, page 2)

2. The present study was carried out using one of the SLR methods most successfully and widely applied in software engineering field. Specially, the Kitchenham's method [30]. This method present rigorous stages to analyze research knowledge using a trustworthy and auditable methodology. Some authors, however, have criticized Kitchenham's method and/or proposed improvements on this one [15], [31].

In the wake of these criticisms and suggestions for improvement, Kitchenham published an updated version of her method in [30]. But, at present, some authors [15] admit that an important gap still exists regarding the evaluation of quality in studies based on empirical methods.

This SLR follows the latest version of Kitchenham's method, referenced above. It describes three phases for executing a systematic review: (1) planning, which defines aspects such as the need for the research, review protocol and research questions; (2) conducting, which the previously established protocol is carried out; and (3) reporting, which presents the final analysis to answer each research question.

Figure 1 shows these phases and their tasks on a timeline to achieve research objective of this article. (Model-Based Software Design and Testing in Blockchain Smart Contracts: A Systematic Literature Review, page 2)

3. A systematic literature review (SLR) was selected as the research method for this study. ''An SLR is a type of secondary study in which primary studies are examined impartially and iteratively to define, interpret, and discuss evidence relevant to the research questions'' [49]. According to Kitchenham [49], [50], an SLR has three main phases: planning, conducting and reviewing the review, as shown in Table 1. Researchers have used the SLR process in several domains [2], [51]- [55].

The authors of this work completed all three phases of the SLR. Inter-rate reliability analyses were undertaken during the initial and final selection phases of the SLR to reduce inter-person bias. The findings of the inter-rater reliability review are discussed in Section 3.2. We followed all of the processes in the three phases of the SLR, as stated in Table 1.

TABLE 1. SLR phases. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 4)

4. There are two different techniques to identify the primary sources for literature review studies [44]. In the first technique, which is common in the software engineering community, search strings are developed and then executed on different digital libraries (e.g., ACM Digital Library) [45].

The second one is more common in the information systems community and starts with identifying a pool of initial papers, followed by the backward snowballing technique [23]. Jalali and Wohlin [44] applied both techniques on Agile practices in Global Software Engineering (GSD) and realized that although these techniques led to the identification of different sets of studies, no significant differences were observed in the findings. Human values have been researched in many domains across different research areas. In Section II, we discussed that there is no consensus on what human values are, and there are many values models that cover a different number of human values with various terminologies. Further to this, there is no established theory on human values within the software engineering community [19]. Due to these limitations, it was not possible for us to build a search string that covers all human values and execute it on different digital libraries. Hence, we decided to follow the approach proposed by Webster and Watson in the information systems community, which includes the following two steps [23]. Figure 2 shows our paper collection process. (Operationalizing Human Values in Software Engineering: A Survey, page 6)

5. This systematic review follows a structured approach aligned with prior systematic reviews on LLM-based agents in software engineering [1], [13]. The methodology ensures comprehensive coverage of relevant literature while maintaining rigor and transparency throughout the review process. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 3)

6. FIGURE 1. Steps of the systematic literature review process.

Gambar tersebut menampilkan langkah-langkah proses tinjauan literatur sistematis dalam format diagram alir. Diagram ini terdiri atas beberapa langkah yang disajikan secara linear, dengan koneksi antar langkah menggunakan garis berwarna biru.

Pertama-tama, gambar menunjukkan langkah persiapan (Preparation), yang mencakup identifikasi topik penelitian dan perumusan pertanyaan penelitian. Langkah ini diikuti oleh langkah pencarian literatur, yaitu proses pengumpulan dan seleksi artikel yang relevan dengan topik penelitian.

Selanjutnya, gambar menampilkan langkah analisis data, dimana hasil dari literatur yang dipilih akan dianalisis untuk mengidentifikasi temuan-temuan penting. Langkah ini diakhiri dengan konfirmasi keabsahan dan kualitas hasil penelitian, yang merupakan langkah yang sangat penting dalam proses tinjauan literatur sistematis.

Terdapat beberapa elemen yang tampak pada gambar ini, seperti simbol-simbol yang merepresentasikan masing-masing langkah, serta garis-garis yang menghubungkan antar langkah. Namun, tidak terdapat angka atau label penting yang menonjol dalam diagram ini.

Makna singkat dari gambar ini adalah sebagai peta proses tinjauan literatur sistematis, memberikan panduan langkah demi langkah untuk mengembangkan penelitian dan memastikan kualitas hasilnya. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 5)

7. The SLR was conducted to extract critical success factors, barriers, and implementation practices from the literature. Rockart [38] defined SLR as a method of systematically collecting, analyzing, and reporting data from the literature of a specific research area and questions of interest [38].

The SLR technique was used to search for the most relevant literature by applying explicit inclusion and exclusion criteria for primary studies [38].

We followed the guidelines provided by Rockart [38] to conduct our SLR study. The approach consists of three main phases: planning, conducting, and reporting the review. A thorough discussion of the SLR study conducted for this research project can be found in our previously published articles [25], [63], [64]. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 3)

8. TABLE 1. Rank wise comparison of success factors across SLR and empirical study.

Data di dalam tabel menampilkan perbandingan antara faktor keberhasilan (success factors) dari studi literatur sistematis (SLR) dan penelitian empiris. Ada dua kolom utama yang dapat dilihat, yaitu peringkat (rank) untuk setiap faktor keberhasilan di SLR dan penelitian empiris.

Dari data yang tersedia, tidak ada informasi tentang variabel/kolom yang lebih spesifik selain nama-nama faktor keberhasilan. Namun, nilai atau pola penting dapat dilihat dari perbandingan antara kedua metode. Contohnya, faktor "SF20: proses evaluasi peningkatan" menerima peringkat yang lebih tinggi di penelitian empiris dibandingkan dengan SLR.

Insight singkat yang dapat disimpulkan adalah bahwa ada perbedaan dalam prioritas penilaian faktor keberhasilan antara studi literatur sistematis dan penelitian empiris. Penelitian ini menunjukkan pentingnya memahami bagaimana praktisi melihat kriteria keberhasilan dalam implementasi proses perbaikan software, yang berbeda dari apa yang telah ditulis di literatur. (SPIIMM: Toward a Model for Software Process Improvement Implementation and Management in Global Software Development, page 5)

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 29

- conversation_id: 13
- user_chat_id: 537
- bot_chat_id: 538

### user_input

Apa itu software development?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 30

- conversation_id: 13
- user_chat_id: 539
- bot_chat_id: 540

### user_input

Apa tujuan software development?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 31

- conversation_id: 13
- user_chat_id: 541
- bot_chat_id: 542

### user_input

Bagaimana proses software development dilakukan?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 32

- conversation_id: 13
- user_chat_id: 543
- bot_chat_id: 544

### user_input

Mengapa software development membutuhkan software testing?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 33

- conversation_id: 13
- user_chat_id: 545
- bot_chat_id: 546

### user_input

Apa hubungan software development dengan software engineering?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 34

- conversation_id: 13
- user_chat_id: 547
- bot_chat_id: 548

### user_input

Bagaimana Agile software development mempercepat software development?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 35

- conversation_id: 13
- user_chat_id: 549
- bot_chat_id: 550

### user_input

Mengapa software quality harus diperhatikan sejak awal software development?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 36

- conversation_id: 13
- user_chat_id: 551
- bot_chat_id: 552

### user_input

Bagaimana software metrics membantu memantau software development?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

4. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

5. Kupiainen et al. [22] conducted a systematic review of the use and impact of software metrics in ASD in industry. The authors reported that software metrics are mainly used for sprint planning, tracking progress, improving software quality, fixing software process, and motivating people. The authors reported that metrics like velocity, effort estimation, customer satisfaction, defect count, technical debt and build are used prominently in ASD. In their systematic review, Tahir et al. [46] observed that metrics for defects, effort, size, duration, productivity, employee commitment, and customer satisfaction are commonly reported in the state of the art. These findings complement another review by Gómez et al. [15], where complexity and size were found to be the most measured attributes in MPs. Other usage of metrics in ASD discussed in the literature are for planning and tracking software development [22], understanding development performance and product quality [48], measuring process quality [50], estimating effort [47], and reporting progress and quality to stakeholders not involved in the actual development [4]. Taken together, metrics targeting sprint planning, fixing software process, effort estimation, development performance, and software defects can be used to measure an organization's process performance. However, this objective is not expressly stated in any of the reviews mentioned above. On the contrary, [22] remarked that more studies are needed to explore the rationale behind utilizing the metrics the authors found in their review. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 3)

6. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. We observed that the metrics strategy solutions were the most frequently used in identifying the architectural decay, thereby these metrics can determine the architectural instability growth with the system evolution, identify the probability of the classes contributing to architectural inconsistencies, and diagnose the anomalies, whether agglomerations or individual is more correlated to architectural problems. However, the use of current metrics at the class level may be affected by size bias significantly and inefficiency automatically in detecting architectural problems, indicating that the most likely cause is the problem on how these metrics are implemented through tools and reconsideration in specifying the selection of the appropriate metrics at different locations of software components, especially when compared to the same results that achieved efficiency manually. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 22)

8. Once the selection was made, at each Scrum Team retrospective meeting, the team usually spends 15 to 20 minutes on visualizing and analysing these selected process metrics. Process metrics are a great fit since this part of the meeting is devoted to people, processes, tools, lessons learnt and how to improve the way of working. Of course the role of the Product Owner and Scrum Master is to make those discussions and displays interesting, but this turned out to be an easy job for them, because developers usually like statistics and some trends/graphs, such as those shown in the previous section. These results, trends and metrics values are used to motivate the team and improve the process, and also to find the problems in order to resolve them. (Measuring and Improving Agile Processes in a Small-Size Software Development Company, page 1)

### response

Software metrics membantu memantau software development dengan menyediakan informasi tentang kualitas dan kompleksitas software, sehingga dapat memprediksi kemungkinan kesalahan klas serta mendukung pengambilan keputusan selama siklus hidup perangkat lunak (SDLC).

### reference


---

## Sample 37

- conversation_id: 13
- user_chat_id: 553
- bot_chat_id: 554

### user_input

Apa peran software maintenance setelah software development selesai?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Release and deployment are two distinct processes in the project's lifecycle. We still regard security activities as a single phase, even though there isn't much work to be done in this phase. A security assessment is performed before the release of the software. The evaluation's purpose is to find remaining security weaknesses. The study concludes with a review report. The development team fixes the Security flaws found in a review report. A security audit is carried out following the evaluation. Based on the audit report, the management decides on the software release. The software is now available for deployment when it has been released. Security activities are documented in Table 6 [3], [87]- [91] during the release and deployment phases. (Security Assurance Model of Software Development for Global Software Development Vendors, page 1)

3. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

4. The software development activity is a set of procedures that yields software as an outcome. The procedure and standards in the software development have improved over time and practices like CMM (Capability Maturity Model), now CMMI (Capability Maturity Model Integration), is often considered as an industry standard in software development [1]- [3]. Presence of software in computing devices, mobiles, wearable devices and phablets has made software an entity of extreme relevance in running the life's events and the development of software has therefore increased over time. Ebert [4] has identified that the producers and consumers of software applications have increased, software applications have rationally become more customizable to meet requirements of businesses. (Build Software or Buy: A Study on Developing Large Scale Software, page 1)

5. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

6. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

7. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

8. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

### response

Setelah software development selesai, peran software maintenance adalah untuk memperbaiki atau mengoreksi masalah yang ditemukan oleh pengguna atau pengembang. Ini dapat dilakukan secara independen tergantung pada betapa seriusnya masalah tersebut.

(Sumber: Systematic Mapping: Artificial Intelligence Techniques in Software Engineering)

### reference


---

## Sample 38

- conversation_id: 13
- user_chat_id: 555
- bot_chat_id: 556

### user_input

Apa itu software maintenance?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

3. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

4. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

5. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

6. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

7. Software Project Management (SPM) includes a set of activities to deliver a software product and related artifacts (e.g., source code, models, test case, and documentation) to accomplish specific goals while satisfying a set of constraints [1]. A widely used model of SPM constraints, suggested in the Project Management Body of Knowledge (PMBOK), is known as the triple constraint that include cost, time, and scope. In the software industry, it is common to classify projects that satisfy the triple constraint as successful [2]. (Team Formation in Software Engineering: A Systematic Mapping Study, page 1)

8. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

### response

Software maintenance adalah fase yang mengikuti seluruh siklus hidup perangkat lunak. Fase ini terjadi jika pengguna atau pengembang menemukan masalah, maka masalah itu bisa diperbaiki atau dikoreksi sebelum rilis berikutnya, tergantung pada betapa seriusnya masalah tersebut.

(Sumber: Systematic Mapping: Artificial Intelligence Techniques in Software Engineering)

### reference


---

## Sample 39

- conversation_id: 13
- user_chat_id: 557
- bot_chat_id: 558

### user_input

Mengapa software maintenance penting?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

3. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

4. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

5. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

6. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

7. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

8. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

### response

Menurut konteks tersebut, software maintenance penting karena dapat membantu mengurangi biaya dan meningkatkan kualitas software. Biaya perawatan software setiap tahunnya telah meningkat menjadi $312 miliar secara global [17], [18]. Selain itu, software yang tidak dipelihara dengan baik dapat menyebabkan kerusakan pada software dan bahkan kehilangan ekonomi sebesar 1,1 triliun dolar pada tahun 2016 karena kesalahan software [38].

### reference


---

## Sample 40

- conversation_id: 13
- user_chat_id: 559
- bot_chat_id: 560

### user_input

Kapan software maintenance dilakukan?

### retrieved_context

1. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

2. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

3. Before deploying software, administrators first understand the security stance. Some of the identified faults that were not addressed previously will be revisited, prioritized, and corrected after deployment. New threats are tracked during this phase. The software can never be 100 percent secure, and new threats emerge regularly phase [14]. As a result, efforts must be made to secure the software. The maintenance team should keep track of new threats that the system encounters to address them promptly and prevent security breaches [83], [116]. Table 15 presents prescriptive actions to increase security during the maintenance phase of SDLC [14], [65], [105], [114], [117], [118]. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

5. First, a list of factors is finalized for the decision making of software maintenance in the context of global software development. For this purpose the most relevant published literature [4], [6], [7], [8], [10], [14], [15], [16] showing the lists of relevant factors is thoroughly reviewed. After an in-depth analysis the similar factors are merged based on their relevancy and impact on software maintenance that results into a list of 10 factors. In the next step these factors are evaluated to extract their interrelationships, and also utilized in the proposed integrated approach of software maintenance process. (An Integrated Approach for Criteria Evaluation and Software Maintenance Process Management: Insights From Global Software Development Perspective, page 3)

6. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

7. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

8. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 41

- conversation_id: 13
- user_chat_id: 561
- bot_chat_id: 562

### user_input

Apa tujuan software maintenance?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 42

- conversation_id: 13
- user_chat_id: 563
- bot_chat_id: 564

### user_input

Bagaimana software maintenance menjaga software quality?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 43

- conversation_id: 13
- user_chat_id: 565
- bot_chat_id: 566

### user_input

Apa hubungan software maintenance dengan software engineering?

### retrieved_context

1. We group all those articles in this category, which deal with software adherence activities in order to meet new or changed operating environments such as refactoring, maintenance cost estimation, defect correctness, and factors related to software aging (e.g., resource depletion). The SE stages and the number of articles that are associated with those stages are shown in Fig. 3. 136 out of 263 (52%) articles belong to quality assurance and analytic. 44 out of 263 (17%) articles have focused on architecture and design. 29 out of 263 (11%) articles have addressed the implementation followed by requirements engineering stage with 24 out of 263 (9%) articles. 11 (4%) articles were focusing on the maintenance phase. The rest of the articles were not particularly focusing on any stage but were generally applicable to SE. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 5)

2. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

3. From SWEBOK ISO/IEC TR 1975:2015, we adopt the critical knowledge areas in software engineering to use as synonyms for software engineering. Twelve knowledge areas identified from the keywords were selected as most prevalent in the literature. These include software requirements, software design, software construction, software maintenance, software testing, software configuration management, software management, software process, software models and methods, and software quality. This is seen in similar SMSs in software engineering by other researchers Klotins et al. [40]. These formed the first part of the search string, the terminology software was then coined with the Boolean ''AND'' to the terminology identified from the keywords to synonymise engineering, and we used the Boolean OR as presented in Listing 1. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 1)

4. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

5. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

6. A close look at the knowledge areas of software engineering used by the companies as reported in the selected articles indicates that general software development and project management are most prominent in the knowledge area frequency distribution, as presented in Figure 7.

The data detail specifically indicates the most covered knowledge area of software engineering by the articles selected in the study. Figure . 7, illustrates 3 most dominant knowledge areas presenting up to 46 studies identified on the knowledge areas of software development design and construction (33), project management ( 16), and quality (7). The remaining 31 studies covered the knowledge areas of process (5), models and methods (5), maintenance (4), testing (3), requirements (3) and management (1) with the respective number of studies. Although the knowledge areas that ultimately are observed at a point in time are presented decimally in the empirical literature, the initial 10 years show that these knowledge areas are not reflected in the empirical studies around this time. Figure 6(a) shows the studies in the years between 2016 and 2021 present interest in the knowledge area of quality, requirements, models and methods, and maintenance. Although the numbers are minimal, the growing interest of researchers is important for the industry and for the transformation of software development practice in SSCs. (Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework, page 9)

7. The software engineering research will be defined by a more intensive interest in the meta-engineering problems, which include designing processes and systems that can guarantee successful collaboration of the agents and humans in the software creation, maintenance and evolution areas. It can be taken as a transition to the research priorities towards optimization not of single development tasks, but the optimization of the whole ecosystem of human-agent collaboration. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 20)

8. The study of human-computer interaction provides the necessary prerequisites to the creation of more efficient interfaces and cooperative frameworks between humans and autonomous agents, which will overcome the most crucial usability and acceptance issues that currently limit practical implementations. Another critical integration point of software engineering education is the requirement to systematically change the approach to pedagogical practices and curricula to prepare future developers to effectively work with AI-based tools and agents [50]. Additionally, the principles and methodologies existing in software engineering should be periodically updated and extended to control the conduct of agents and to guarantee quality in the AI-influenced development processes [3], [54], [55]. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 17)

### response

Software maintenance adalah salah satu tahapan dalam siklus hidup perangkat lunak yang terkait dengan software engineering. Pada konteks ini, software maintenance meliputi kegiatan seperti prediksi kemantapan perangkat lunak, deteksi penuaan perangkat lunak, dan perkiraan upaya pemeliharaan.

Berdasarkan [Source: A Literature Review of Using Machine Learning in Software Development Life Cycle Stages], software maintenance adalah salah satu tahapan yang kurang difokuskan oleh peneliti dalam domain ini. Namun, pada konteks ini juga disebutkan bahwa research lebih condong ke arah perkiraan biaya/effort daripada tugas pemeliharaan lainnya.

Selain itu, [Source: Software Engineering in Small Software Companies: Consolidating and Integrating Empirical Literature Into a Process Tool Adoption Framework] menyatakan bahwa knowledge area dalam software engineering yang terkait dengan software maintenance adalah salah satu dari 12 knowledge area yang paling berpengaruh.

### reference


---

## Sample 44

- conversation_id: 13
- user_chat_id: 567
- bot_chat_id: 568

### user_input

Bagaimana software metrics membantu proses software maintenance?

### retrieved_context

1. Software metrics make it easy for developers to audit and monitor the quality of software design as the project progresses. In addition, predicting the probability of defective classes is needed to help the software engineers during development to enhance the quality of software and reduce testing and maintenance costs. For example, in order to increase the productivity of software testing, software evaluators can plan tests based on the parts most prone to faults.

TABLE 1. List of inheritance metrics.

Software metrics and fault data for an earlier software version are utilized to make an SFP model for the next software version [83]. When a software has faults, it leades to a disaster because it has a significant human dependency on it. Therefore, there is an emerging requirement for software without faults. Software Companies are expanding to discover faults in software. Producing software without faults is a challenging job. To lower costs and improve software usefulness, it is vital to classify classes which are faulty. Many software metrics are proposed by the researchers to gauge the software quality. In object-oriented paradigm, metrics are beneficial for software engineers to make additional information associated with software quality available. Quality of software can also be monitored through metrics, while software evaluators use metrics to increase the effectiveness of testing [84]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 3)

2. Measurement is needed to validate the effectiveness of software development process. The phrase software metrics describes measurements made on an artifact of software whereas a software artifact has two significant elements: the coded implementation, and the document of its design specification. The initially calculated McCabe, Halstead, and Albrecht metrics, presented during the 1970s, were typically constructed on the coded final software products. Examples of software science metrics include [1] function point analysis [2], and cyclomatic complexity metric [3], which predominated in the early 1980s to measure software product. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

3. Software metrics are foundation to quantify complexity, quality of software, and project costs with effort estimation. Function points and cyclomatic complexity are traditional metrics. These are being utilized in the paradigm of procedure language. Nonetheless, these may not merely be utilized in the context of object-oriented [21]. The procedural languages are less complex while comparing with object-oriented programming language [22]. The majority of studies specified hurdles in moving from a procedural approach towards an objectoriented paradigm [23].In object-oriented, it is problematic to comprehend how inheritance, abstraction, and encapsulation associated with each other. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

4. We observed that the metrics strategy solutions were the most frequently used in identifying the architectural decay, thereby these metrics can determine the architectural instability growth with the system evolution, identify the probability of the classes contributing to architectural inconsistencies, and diagnose the anomalies, whether agglomerations or individual is more correlated to architectural problems. However, the use of current metrics at the class level may be affected by size bias significantly and inefficiency automatically in detecting architectural problems, indicating that the most likely cause is the problem on how these metrics are implemented through tools and reconsideration in specifying the selection of the appropriate metrics at different locations of software components, especially when compared to the same results that achieved efficiency manually. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 22)

5. The software metrics are the basis to measure the complexity, quality of software and estimate cost along with efforts of projects. Traditional metrics such as function point and cyclomatic complexity have been employed in the procedure paradigm. But, these are not simply used in object-oriented paradigm [39], [40]. Object Oriented programming is complex while comparing it with procedural languages [41]. Most studies stated difficulty in switching to the object-oriented paradigm from the procedural approach [42]. In Objectoriented Programming, it is difficult to understand how features, for example abstraction, inheritance and encapsulation relate to each other [43]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

6. The software maintenance stage has been found as the least focused stage for researchers in this domain. In this category, the research is more inclined towards cost/effort estimation than the rest of the maintenance tasks. We found articles focusing on software maintainability prediction, which refers to the proposed ML techniques in order to assist the prediction of maintainability metrics appropriate for specific software projects [45]. Software aging detection refers to the use of ML in order to detect software maturity and its aging in terms of resource depletion such as memory leaks, high CPU usage, and overtime. In this regard, Andrzejak et al. [46] investigated the feasibility of ML techniques for classification in detecting early performance degradation due to software image aging. The maintenance effort estimation class aims at estimating the amount of effort required for the maintenance of a software system using ML, e.g., Chandra et al. [47] used an SVM-based regression model in order to forecast maintenance effort with univariate and multivariate approaches. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 7)

7. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

8. Metrics and roles play a fundamental role in SD, as supported by GAI. The utilization of these metrics enables the establishment of an objective for evaluating the quality of AI-generated codes, including their accuracy and efficiency. These measures empower developers to evaluate the congruence between the resulting artifacts and original objectives, thereby identifying opportunities for enhancement [21], [22]. More broadly, metrics support software engineering quality assessment by quantifying the key characteristics of the development process, including efficiency and maintainability. A review of the literature reveals that commonly reported metrics include structural complexity measures, which assess software architecture using indicators such as the number of modules and interconnections [23]. Quality metrics are used to forecast software reliability and support decision-making throughout the SDLC [24]. Finally, productivity metrics are reported, and these assess the impact of GAI-based tools on development speed, quality, and overall efficiency [6], [25]. (Generative Artificial Intelligence for Software Development Using ISO/IEC 29110 Basic Profile: Gaps and Opportunities, page 2)

### response

Menurut Konteks "A Literature Review of Using Machine Learning in Software Development Life Cycle Stages", software metrics membantu proses software maintenance dengan:

* Memprediksi ketersediaan perawatan untuk memperbaiki maintainability
* Mendeteksi kemungkinan kebocoran sumber daya, seperti kerusakan memori, penggunaan CPU yang tinggi, dan waktu lama
* Mengestimasikan upaya perawatan dengan menggunakan model regresi SVM

### reference


---

## Sample 45

- conversation_id: 13
- user_chat_id: 569
- bot_chat_id: 570

### user_input

Mengapa software testing tetap penting saat software maintenance?

### retrieved_context

1. Software testing covers several activities of the software development processes starting from the validation of initial requirements through to the acceptance of the end product by the customer [9]. Starting from the requirement specifications, the software testing tasks need to be planned and implemented in different stages of the software development process. Furthermore, software testing needs to be performed during different stages of the software development process for different purposes, such as the testing of the software product lines [10] and the graphical user interface [11]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

2. An analysis of the whole software development process reveals that the testing stage has the longest duration and is the most expensive phase [17] involving labor-intensive tasks [18]. As the software testing process is usually performed with limited resources under time constraints, currently, several research studies are being conducted to improve software testing techniques in order to obtain higher-quality and more reliable software products [19]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

3. Testing is defined as ''an activity in which a system is executed under specified conditions, the results are observed or recorded, and an evaluation is made of some aspect of the system'' (ISO/IEC 24765, 2006) [6]. In parallel to this definition of testing, a major task of the software development process, software testing is defined as the process of observing and demonstrating the behavior of a software system for compliance with its specifications [7]. As it requires several strategies and techniques with the involvement of several tools and resources, software testing is also considered as a complex task [8]. The background for this study is given below, summarizing the important role of software testing in the software development life cycle, potential impact of software testing strategies, and review studies conducted on software testing. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 1)

4. Software testing plays an essential role in Software Development Life Cycle (SDLC) as it ensures the quality and correctness of the software system. However, complete testing of a software system is practically not possible as it consumes an enormous amount of time and resources [1], [2]. Furthermore, faults are normally not distributed uniformly across software modules. Therefore, it is mostly inefficient or impossible to spend the same amount of testing resources and efforts on every individual software module of the system under test. To overcome this problem, Software Fault Prediction (SFP) has been introduced to early identify faulty software modules prior to the testing phase so that the allocation of testing resources can be economically optimised. (Error-Type—A Novel Set of Software Metrics for Software Fault Prediction, page 1)

5. Software testing is usually conducted in the three stages of creating, executing and evaluating the test cases [12], [13]; thus, the creation of appropriate test cases is critical [14], [15]. In other words, the appropriateness of test cases with software features, such as the technology used, the domain in which the software will be used, and the end-user skills is a critical factor in a successful testing process. Matalonga et al. defined the following seven elements to compose a test case: item (product/functionality under test), input (input variables that will stimulate the test item, output (response returned by the test item after receiving a test input), oracle (expected result, predicted behavior under specified conditions based on its specification or another source), result (comparison between the test output and the test oracle), environment (facilities, hardware, software, firmware, procedures, and documentation intended for or used to perform the software testing), and script (procedure specification for manual or automated testing) [16]. (Evolution of Software Testing Strategies and Trends: Semantic Content Analysis of Software Research Corpus of the Last 40 Years, page 2)

6. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

7. As time progresses and technology continues to develop, software has become an increasingly integral part of our daily lives. It is crucial that software functions correctly for endusers, making the assessment of software reliability a critical step in the testing phase. To accurately predict software reliability, various SRGMs have been proposed to describe the process of fault detection and correction [1], [2], [3]. It is important to note that there are still many SRGMs published in the literature. These models vary in terms of their underlying assumptions, mathematical formulations, and applicability to different types of software systems. (Using Modified Diffusion Models for Reliability Estimation of Open Source Software, page 3)

8. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

### response

Tidak ada jawaban langsung terkait pertanyaan user. Namun, dapat ditemukan beberapa fakta yang mendukung pentingnya software testing dalam konteks lain.

- Dalam sumber [Source: Error-Type—A Novel Set of Software Metrics for Software Fault Prediction], disebutkan bahwa software testing sangat penting karena memastikan kualitas dan akurasi sistem perangkat lunak. Namun, tidak ada jawaban langsung terkait pentingnya software testing dalam konteks pemeliharaan.
- Dalam sumber [Source: Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review], disebutkan bahwa agen otomatis saat ini menangani tugas pemeliharaan perangkat lunak yang dulunya memerlukan banyak waktu dan keahlian manusia. Namun, tidak ada jawaban langsung terkait pentingnya software testing dalam konteks pemeliharaan.

Jawaban: Informasi tersebut tidak ditemukan pada dokumen yang tersedia.

### reference


---

## Sample 46

- conversation_id: 13
- user_chat_id: 571
- bot_chat_id: 572

### user_input

Bagaimana software development yang buruk dapat menyulitkan software maintenance?

### retrieved_context

1. Software quality is the total characteristics of an entity that depends on its capacity to satisfy explicit and implicit VOLUME 10, 2022 needs [34]- [36]. Hence, poor software quality negatively impacts not only customer satisfaction but also software maintainability, economic gains, and human life in the real-world context [12], [34], [37], [38]. Software maintenance is the most expensive activity in the software development process, representing about 75% of the total cost. Investing in maintenance and defect prevention efforts is critical because software defects have a detrimental effect on the proper functioning of the software. For instance, the world economy has lost 1.1 trillion dollars in 2016 because of software defects, and an estimated 4.4 billion people were affected [38]. A recent report by the Consortium for Information and Software Quality puts the total financial damage caused by poor quality software at 2.08 trillion dollars in 2020 in the US alone [39]. (How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success, page 2)

2. A bug in a software program is a failure or fault that prevents the program from running as intended, for example, generating an incorrect result. A software fault is a defect that causes a software failure at runtime. A strategy is needed to predict faults earlier, as it helps to reduce faults and improve the quality of software. The essential part of software development is to ensure that developed software has enhanced quality. It is a well-proven fact that the sooner a fault is detected, the sooner it is resolved, the lesser it costs [1]. (Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction, page 1)

3. Vulnerability-oriented architectural research provides a systematic and thorough approach to evaluating a wide variety of possible vulnerabilities, but it is time-consuming and costly [91]. For estimating the severity and cost of security threats, Table 9 presents, some maintenance and stakeholder considerations may be considered [78], [91], [103].

Software development iterations are of limited time, often few weeks, which makes fitting security activities (e.g., security requirement elicitation) challenging because they are often time-consuming'' [65]. Furthermore, defining security policies takes time and raises the cost of software development [65]. Some of the common issues due to

TABLE 11. (Continued.) Secure design practices (SDP).

time pressure in the secure software development process are [65], [83],

i. Organizations compromise security activities to accommodate the accelerated releasing schedule ii. Timing attacks iii. Insufficient time for the teams to get to the security activities iv. pressure to deliver to tight deadlines. (Systematic Literature Review on Security Risks and its Practices in Secure Software Development, page 1)

4. Software development and evolution is a dynamic process and is characterized by change. Software projects often begin with unclear, ambiguous, and incomplete requirements which give rise to intrinsic volatility [1]. Meanwhile, the project team members, software users, environment and technologies are also likely to change throughout the life of the project as different versions of their software are released. When these important factors change and affect the software products, projects, and processes, these changes must be carefully planned [2]. Especially, when additions, deletions and modifications are made to previous generated or in process project artifacts, additional time investment, scrapped effort, and even bugs can result. Therefore, it is important to understand the changing dynamics overtime, the complex interaction effects, and to find the way to control the negative effects of the changes. System dynamics (SD) modeling is one of the best techniques to enable project personnel to software process and model change effects and run the models to better understand the implications of candidate project strategies and decisions [3]. (Change-Oriented Open Source Software Process Simulation, page 1)

5. SA degrades as the system evolves [26]. Interestingly, the eroded architecture impulses the system to complexity, difficulty, and frequent changes than before [27]. The repeated architectural decay leads to a shortening lifetime of the system or rather affects the architecture entirely, resulting in redesigning the architecture of the system from scratch [28]. As a consequence, the SA of system erode over time. This phenomenon is known as architectural degeneration [23], [29], design erosion [30], architectural erosion [11], [23], [31], drift [15], [23], [32], mismatch [33], architectural decay [34], design decay [35], code decay [12], [27], software entropy [36], architecture erosion (or decay) [37], software architecture degradation [9], [15], [38] or software aging [11]. (Software Architecture Degradation in Open Source Software: A Systematic Literature Review, page 3)

6. According to a 2013 study by the University of Cambridge [17], [18], the global cost of finding and removing bugs from software has risen to $312 billion annually, and it makes up half of the development time of the average project. Furthermore, constant change makes matters worse. Changes are the main causes of software bugs and major issues faced by the software industry. Studies conducted by Javed et al. [1] indicated that there is a significant relationship between change requests and overall bugs. Based on Mozilla quality assurance process [19], the focus of the quality assurance is correcting bugs. Therefore, based on these studies, our Quality Assurance Subsystem is modeled and depicted in Figure 7. (Change-Oriented Open Source Software Process Simulation, page 1)

7. The maintenance phase follows the entire life cycle of the software. If users or developers find a problem, it may be fixed or corrected ahead of the next release, depending on how serious it is. (Systematic Mapping: Artificial Intelligence Techniques in Software Engineering, page 4)

8. Autonomous agents are now tackling software maintenance jobs that used to demand a lot of human time and expertise. The most ambitious of these are bug-fixing agents. They comb through error logs, look for patterns in failures, pinpoint the offending lines of code and generate their own fixes so the software keeps running smoothly [22], [38], [39]. Other agents focus on improving code quality. They detect ''code smells,'' suggest better designs and carry out refactoring work that would otherwise be slow and error-prone for human developers [40]. There are also migration agents that help organisations modernise legacy software by adapting it to new platforms, updated libraries or newer language versions [2]. Recent studies show that large language models can even serve as lightweight testers, reproducing bugs with very little input to aid automated debugging [33]. Taken together, these maintenance agents help keep software up to date while cutting down on the technical debt that can build up in large systems. (Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review, page 13)

### response

Software development yang buruk dapat menyulitkan software maintenance karena:

• Menghasilkan software dengan kualitas rendah, sehingga memerlukan biaya besar untuk perbaikan dan pemeliharaan.
• Meningkatkan kemungkinan terjadinya kerusakan software, yang dapat menyebabkan kerugian ekonomi yang signifikan. Contohnya, dunia ekonomi telah kehilangan 1,1 triliun dolar pada tahun 2016 karena kerusakan software.
• Membutuhkan waktu dan biaya besar untuk perbaikan dan pemeliharaan software.
• Meningkatkan kompleksitas sistem software, sehingga sulit untuk diubah atau diperbarui.

Sumber: [Source: How Software Quality Mediates the Impact of Intellectual Capital on Commercial Open-Source Software Company Success], [Source: Experimental Validation of Inheritance Metrics’ Impact on Software Fault Prediction], dan [Source: Systematic Literature Review on Security Risks and its Practices in Secure Software Development]

### reference


---

## Sample 47

- conversation_id: 13
- user_chat_id: 573
- bot_chat_id: 574

### user_input

Apa itu deep learning?

### retrieved_context

1. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Many kinds of research attempt to find solutions for the current obstacles of Machine Learning Systems. To draw optimal decision making, approaches such as Fault Tree Analysis, Fuzzy Logic, Metaheuristic Algorithm, and Artificial Neural Network are developed to test with a huge amount of training data by using different algorithms. However, the sufficiency and versatility of Deep Learning systems are based on the accuracy of the test data set. It is difficult to provide adequate support due to the accessibility of test data quality issue. The current Deep Learning systems have various vulnerabilities and their system analysis and defect detection are extremely difficult. Unlike traditional software systems, Machine Intelligence does not have a clear controllable logic and understandability since the process to make decisions rely on the training data. The recent study shows two major vulnerabilities in Deep Learning systems: Software quality from the output of Deep Learning alone is not adequate; and Failure in unseen attacks even though Deep Learning is immune to known types of attacks [18], [19]. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

3. Software Defects Prediction (SDP) consists in identifying defective software components, being considered an essential activity during software development. It represents the activity of identifying defective software modules in new versions of a software system [1]. SDP is considered of great importance in software engineering, as it contributes to continuously improving the software quality. Developing high quality software systems is expensive and, in this context, SDP is used for increasing the cost effectiveness of quality assurance and testing [2]. By detecting fault-prone modules in new versions of a software system, SDP helps to allocate the effort so as to test more thoroughly those modules [1]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

4. Table 12 presents, for each classiﬁer c ∈{ DL-FASTAI, Table 12 memaparkan hasil analisis dari beberapa jenis klasifikator dalam penggunaan prediksi kelemahan perangkat lunak berbasis deep learning. Dua variabel utama yang diperhatikan adalah "sensitivity" (Sens) dan "AUC" (Area Under Curve). Sensitivity merupakan ukuran yang menunjukkan kemampuan klasifikator dalam mendeteksi kasus kelemahan yang sebenarnya. Sementara itu, AUC merupakan indikasi performa yang lebih komprehensif, menunjukkan kemampuan klasifikator untuk membedakan antara kasus kelemahan dan non-kelemahan.

Dari data yang tersedia, tidak ada informasi yang cukup spesifik tentang nilai-nilai khusus dari Sens dan AUC untuk setiap klasifikator. Namun, perlu diingat bahwa hasil analisis ini mungkin membantu para peneliti memahami pola umum performa antara berbagai jenis klasifikator dalam konteks prediksi kelemahan perangkat lunak dengan menggunakan deep learning. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 14)

5. Deep learning-based approaches show great potential to address power line inspection tasks. However, existing work still faces challenges with the complex backgrounds and real-time applications. Additionally, considering the timing and computational resource constraints, further exploration is necessary to develop a resource-efficient model that can be deployed on UAVs, ensuring efficient processing and reliable communication between the UAV and the ground station. The literature study highlights the necessity of developing a complete scheme that ensures connectivity, privacy, and security in the communication between the UAV and ground station, as well as developing a model that is accurate and light enough to mount to a UAV. (LCUT-Sv9: UAV-Assisted Powerline Inspection Framework with Secure Time-Sensitive Communication for Industry 5.0, page 4)

6. Apart from communication paradigms, DeepLabV3 and a modified U-Net were used to enhance efficiency and reliability with UAV imagery segmentation tasks, significantly improving the accuracy and robustness [9]. TLSUNet combined U-Net with a lightweight backbone structure and contextual information features to optimize segmentation tasks by reducing computational complexity while maintaining high accuracy [10]. A lightweight segmentation network was introduced for the real-time detection of broken strands on power lines, thus enhancing the efficiency of inspection processes [11]. Recent research combined attention mechanisms with a dual-branch approach to improve detection. It achieved high accuracy in segmenting power lines and towers using Light Detection and Ranging (LiDAR) data from UAVs, leveraging multiscale density features and pointbased deep learning techniques [12]. (LCUT-Sv9: UAV-Assisted Powerline Inspection Framework with Secure Time-Sensitive Communication for Industry 5.0, page 2)

7. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

8. The current section starts by describing, in Section III-A, the publicly available data sets used as case studies for SDP. Section III-B reviews existing supervised machine learning-based solutions for SDP. The section ends with a description of the features used for SDP, both manually and automatically engineered ones.

The prediction of defects in software systems is a highly active research area. For instance, Hall et al. [7] have identified, in a systematic review of SDP, 208 studies on defect prediction, all published between 2000 and 2010, and numerous other studies have been published since then.

There is a great interest in developing new highperformance software defect predictors. Besides the interest in developing accurate and robust defect predictors, there is also interest in defining new relevant software features on the basis of which to distinguish between defective and non-defective software modules. Therefore, the research efforts in the field of SDP take one of the following two directions: proposing new accurate classifiers or designing new relevant features [11]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

### response

Deep Learning adalah desain yang terus menerus menganalisis data dengan struktur logika seperti bagaimana manusia dapat menarik kesimpulan. Deep Learning membutuhkan jumlah besar data untuk menggunakan input dalam algoritma sehingga menghasilkan prediksi yang lebih akurat.

### reference


---

## Sample 48

- conversation_id: 13
- user_chat_id: 575
- bot_chat_id: 576

### user_input

Mengapa deep learning digunakan?

### retrieved_context

1. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Many kinds of research attempt to find solutions for the current obstacles of Machine Learning Systems. To draw optimal decision making, approaches such as Fault Tree Analysis, Fuzzy Logic, Metaheuristic Algorithm, and Artificial Neural Network are developed to test with a huge amount of training data by using different algorithms. However, the sufficiency and versatility of Deep Learning systems are based on the accuracy of the test data set. It is difficult to provide adequate support due to the accessibility of test data quality issue. The current Deep Learning systems have various vulnerabilities and their system analysis and defect detection are extremely difficult. Unlike traditional software systems, Machine Intelligence does not have a clear controllable logic and understandability since the process to make decisions rely on the training data. The recent study shows two major vulnerabilities in Deep Learning systems: Software quality from the output of Deep Learning alone is not adequate; and Failure in unseen attacks even though Deep Learning is immune to known types of attacks [18], [19]. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

3. Behavioral cloning [56,61] is used to supervised fine-tuning the Reranker by mimicking expert trajectories, allowing the model to learn the fundamental actions required for effective ranking. In this stage, the Reranker focuses on learning how to predict the correct intermediate actions a t based on the given task and context. To achieve this, the Reranker is trained on a dataset of expert demonstrations, denoted as D e . This enables the model to acquire basic instruction-following capabilities and leverage prior knowledge. The training objective is to maximize the likelihood of the expert's document selection decisions: (DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation, page 1)

4. The rationality of hyper-parameter settings in deep learning depends on several factors such as the problem at hand, the size of the dataset, the complexity of the model, and the computational resources available. Regarding the use of ReLU as an activation function and 100 nodes in an Artificial Neural Network (ANN), these are common choices that have been shown to work well in many applications. ReLU is a popular choice for an activation function because it has been shown to be effective in addressing the vanishing gradient problem and allows for faster training compared to other activation functions like sigmoid or tanh. Additionally, ReLU has a sparsity-inducing effect which can lead to better generalization performance. The choice of 100 nodes in an ANN depends on the complexity of the problem and the size of the dataset. If the problem is relatively simple or the dataset is small, then 100 nodes may be more than enough to capture the underlying patterns in the data. However, if the problem is more complex or the dataset is large, then a larger number of nodes may be necessary to capture the complexity of the problem. (Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy, page 11)

5. Software Defects Prediction (SDP) consists in identifying defective software components, being considered an essential activity during software development. It represents the activity of identifying defective software modules in new versions of a software system [1]. SDP is considered of great importance in software engineering, as it contributes to continuously improving the software quality. Developing high quality software systems is expensive and, in this context, SDP is used for increasing the cost effectiveness of quality assurance and testing [2]. By detecting fault-prone modules in new versions of a software system, SDP helps to allocate the effort so as to test more thoroughly those modules [1]. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 1)

6. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

7. Deep learning-based approaches show great potential to address power line inspection tasks. However, existing work still faces challenges with the complex backgrounds and real-time applications. Additionally, considering the timing and computational resource constraints, further exploration is necessary to develop a resource-efficient model that can be deployed on UAVs, ensuring efficient processing and reliable communication between the UAV and the ground station. The literature study highlights the necessity of developing a complete scheme that ensures connectivity, privacy, and security in the communication between the UAV and ground station, as well as developing a model that is accurate and light enough to mount to a UAV. (LCUT-Sv9: UAV-Assisted Powerline Inspection Framework with Secure Time-Sensitive Communication for Industry 5.0, page 4)

8. With the rapid development of information technology, the scale of data appears explosive growth. Mining valuable information from complex data has great practical significance [1]. As an important method in the field of data mining, clustering algorithm is widely used in data analysis and mining. DBSCAN algorithm is a typical clustering algorithm, and data density is as a measure, which can identify arbitrary shape classes and noise points of data sets. Some data show that by 2020, the data accumulated by China will account for 20% of the global data. Nowadays, both the government and enterprises have accumulated a large amount of data [2], and mining useful information from these data has great research value. As an important technology in the field of data mining, clustering has been applied in many fields, such as pattern recognition, information retrieval, network public opinion prediction and so on. (DBSCAN-Based Automatic De-Duplication for Software Quality Inspection Data, page 1)

### response

Deep Learning digunakan untuk menganalisis data dengan struktur logika yang mirip dengan cara manusia mengambil kesimpulan. Dalam proses ini, deep learning memerlukan jumlah besar data set sebagai input dalam algoritma untuk mencapai prediksi yang lebih akurat.

### reference


---

## Sample 49

- conversation_id: 13
- user_chat_id: 577
- bot_chat_id: 578

### user_input

Apa perbedaan deep learning dan machine learning?

### retrieved_context

1. Deep Learning is designed to continually analyze data with a logic structure as mimicking how a human can draw a conclusion. The deep learning needs a huge number of data sets to use input in the algorithms in order to result in a more accurate prediction. For instance, Google's AlphaGo, a sharp intellect and intuition game, learns by itself without predefined data. It makes a more specific move and becomes the greatest player of all. Deep Learning defines a new paradigm based on data-driven programming. Since Machine Intelligence or Deep Learning depends on the training data, the accuracy and quality of data play a vital role for public safety using machine learning in autonomous vehicles. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

2. Many kinds of research attempt to find solutions for the current obstacles of Machine Learning Systems. To draw optimal decision making, approaches such as Fault Tree Analysis, Fuzzy Logic, Metaheuristic Algorithm, and Artificial Neural Network are developed to test with a huge amount of training data by using different algorithms. However, the sufficiency and versatility of Deep Learning systems are based on the accuracy of the test data set. It is difficult to provide adequate support due to the accessibility of test data quality issue. The current Deep Learning systems have various vulnerabilities and their system analysis and defect detection are extremely difficult. Unlike traditional software systems, Machine Intelligence does not have a clear controllable logic and understandability since the process to make decisions rely on the training data. The recent study shows two major vulnerabilities in Deep Learning systems: Software quality from the output of Deep Learning alone is not adequate; and Failure in unseen attacks even though Deep Learning is immune to known types of attacks [18], [19]. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 1)

3. AI-based machine learning requires a huge number of inputs as the knowledge and different intelligent algorithms in order to make the right decision. By looking at an example using technology in unmanned vehicles, there will be a basic understanding of how machine learning or machine intelligence work. The development of machine intelligence is still far from mimicking the cognitive competence of the human brain. It is still challenging to deal with those data effectively and making a driving decision accurately and quickly [17]. Machine learning sometimes returns an inaccurate prediction based on the collection of training data and an engineer needs to make some adjustments to avoid significant losses in terms of public safety. (Testing and Quality Validation for AI Software–Perspectives, Issues, and Practices, page 5)

4. In the future, we intend to perform a more comprehensive study investigating the relationship between ML and SDLC stages. To this end, we intend to narrow down our search query by including ML terms such as classification, regression, SVM, ANN, inductive logic, Bayesian network, or deep belief network. We believe in this way, we can grasp a more focused view of the state-of-the-art. (A Literature Review of Using Machine Learning in Software Development Life Cycle Stages, page 18)

5. Due to the severe imbalancement of the two classes (the number of defects are highly outnumbered by the number of non-defective ones), the main difficulty is that of predicting the positive class. Therefore, we consider, as the real difficulty, the one on the positive class. A difficulty of 1.0 means that every instance of the respective class has as its nearest neighbour an entry from the other class. That level of dissimilarity between positive entries makes it incredibly difficult for a classification model to correctly identify that class. It can be observed that some data sets have difficulties that come close to 1.0, while for all of them, the positive entries are mostly surrounded by negative ones (difficulty > 0.5). (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 7)

6. The application of AI in automated code analysis has also led to significant advancements in early vulnerability detection, thereby strengthening security across SE workflows. In particular, [38] highlights the importance of machine learning (ML) and deep learning (DL) techniques in identifying security vulnerabilities and advocating for hybrid systems that enhance detection accuracy. Similarly, [39] emphasizes how Natural Language Processing (NLP) and DL can aid software vulnerability assessments, resulting in improved resource management and more informed risk evaluation decisions. AI has also revolutionized design and development tasks by automating complex processes. Reference [37] presents a deep learning-based technique for transforming graphical user interface (GUI) mock-ups into operational prototypes, thus simplifying the interface design process. In another example, [39] introduces FLASH, a model-based approach to optimize software configurations to enhance speed and resource efficiency. Furthermore, [40] employs the Non-dominated Sorting Genetic Algorithm III (NSGA-III) for software re-modularization, refining the software architecture, reducing code modifications, and improving overall consistency. (Impact of Artificial Intelligence on Software Engineering Phases and Activities (2013–2024): A Quantitative Analysis Using Zero- Truncated Poisson Model, page 3)

7. Table 12 presents, for each classiﬁer c ∈{ DL-FASTAI, Table 12 memaparkan hasil analisis dari beberapa jenis klasifikator dalam penggunaan prediksi kelemahan perangkat lunak berbasis deep learning. Dua variabel utama yang diperhatikan adalah "sensitivity" (Sens) dan "AUC" (Area Under Curve). Sensitivity merupakan ukuran yang menunjukkan kemampuan klasifikator dalam mendeteksi kasus kelemahan yang sebenarnya. Sementara itu, AUC merupakan indikasi performa yang lebih komprehensif, menunjukkan kemampuan klasifikator untuk membedakan antara kasus kelemahan dan non-kelemahan.

Dari data yang tersedia, tidak ada informasi yang cukup spesifik tentang nilai-nilai khusus dari Sens dan AUC untuk setiap klasifikator. Namun, perlu diingat bahwa hasil analisis ini mungkin membantu para peneliti memahami pola umum performa antara berbagai jenis klasifikator dalam konteks prediksi kelemahan perangkat lunak dengan menggunakan deep learning. (An in-Depth Analysis of the Software Features’ Impact on the Performance of Deep Learning-Based Software Defect Predictors, page 14)

8. Typically machine learning focus on design and development of algorithms with techniques. That extricate rules, and patterns from massive databases. Neural Networks (NN) are previously being utilized within the software to create reliability growth models for the prediction of total modification or reusability metrics. The NN model is trained to do again a stipulated series of exact instances classification, as an alternative to creating formulas or rules. Mahajan et. al [38] mentioned that machine learning methods are beneficial to determine software faults as complete processing is performed by the computer. (Efficacy of Inheritance Aspect in Software Fault Prediction—A Survey Paper, page 1)

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 50

- conversation_id: 13
- user_chat_id: 579
- bot_chat_id: 580

### user_input

Apa manfaat deep learning dalam pengembangan AI?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 51

- conversation_id: 13
- user_chat_id: 581
- bot_chat_id: 582

### user_input

Bagaimana deep learning berhubungan dengan CNN?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

## Sample 52

- conversation_id: 13
- user_chat_id: 583
- bot_chat_id: 584

### user_input

Mengapa CNN sering digunakan dalam deep learning?

### retrieved_context

-

### response

I apologize, but I encountered an error processing your request.

### reference


---

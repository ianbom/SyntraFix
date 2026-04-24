# RAGAS Test Data

File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.
`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.
`reference` sengaja dikosongkan agar dapat diisi manual.

## Sample 26

- conversation_id: 13
- user_chat_id: 649
- bot_chat_id: 650

### user_input

Apa itu CNN?

### retrieved_context

1. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

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

2. Qurishee [71] presented an autonomous pavement condition evaluation employing deep learning, an unmanned aerial vehicle (UAV), and Raspberry Pi tiny computer technologies, which improves road maintenance and renovation management efficiency and cost effectiveness. A lowcost Raspberry Pi smart defect-detecting camera was set up with the trained SSD MobileNet v1, which can be deployed with a UAV for real-time and remote pavement condition inspection. According to preliminary data, the smart pavement detector camera achieves 60% accuracy at 1.2 frames per second on the Raspberry Pi and 96% accuracy at 13.8 frames per second on a CPU-based computer. Hassan et al. [72] employs CNN models that are improved tiny YOLO V3 on UAVs and achieves good results, with precision, sensitivity, and F1 score values better than 85%, but without considering FPS. Sathvik et al. [39] introduce

TABLE 1. Comparison of object detection models deployed on edge device.

pothole detection, an edge computing framework that runs efficient deep neural networks, lowering the latency of earlier techniques. Using transfer learning-based models, an F1 score of 0.64. The YOLO V7 model had an F1 score of 0.51, which improved proportionally (the higher the F1 score, the more efficient the training model) as the number of epochs increased. The YOLO V7 runs on a CPU-based computer, however it does not consider run on edge devices.

Several studies using CNN models deployed on NVIDIA Jetson Nano devices include the SSD-MobileNet model with a batch size of 64 and mAP of 0.22 [48], the MobileNet V2 model, and the SSD Resnet50V1 model [34], [35]. The MobileNet V2 model using hyperparameter settings has a higher mAP of 0.0869 and average recall 0.241 than the SSD Resnet50V1. Yebes et al. [40] created a massive dataset of images with pothole annotations and road scenes from many cities across the world, captured with various cameras, vehicles, and viewpoints under varying environmental circumstances. Their fine-tuned Faster R-CNN Inception v2, Faster R-CNN Resnet101, and Faster R-CNN Inception-Resnet v2 models reached precision 75%, and their CNN model deployed the pothole detector on the Nvidia DrivePX2 platform running at 5-6 frames per second. Based on the findings of this investigation, CNN models were included in the hardware, as indicated in Table 1, although further research is needed to improve system performance (mAP, AR, F1 score) and speed up inference time. Based on previous studies on road damage, several researchers have utilized the CNN model by optimizing its network structure. Specifically, the YOLO model automates the network structure through the introduction of a new module. However, few YOLOv3 models incorporate hyperparameter optimization, with only one study utilizing the Bayesian method. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 1)

3. FIGURE 6. CNN block diagram.

Gambar ini menampilkan skema blok CNN (Convolutional Neural Network). Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar. Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi).

Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. Namun, detail tentang jenis citra yang digunakan sebagai input masih tidak dapat diidentifikasi secara pasti dari gambar ini.

Dari skema blok CNN ini, dapat disimpulkan bahwa proses pemrosesan gambar dilakukan melalui beberapa tahap konvolusi dan downsampling dengan maksimum. Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori.

Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Oleh karena itu, interpretasi harus berfokus pada gambaran umum proses yang terjadi dalam CNN daripada detil teknis parametris. (Development of a Speech Emotion Recognition Dataset for Indonesian, page 6)

4. FIGURE 8. Confusion matrix result of ball detection using CNN. FIGURE 8. Confusion Matrix Hasil Deteksi Bola Menggunakan CNN.

Gambar ini menampilkan sebuah grafik yang disebut "confusion matrix". Grafik ini digunakan untuk mengukur akurasi model klasifikasi, yaitu model CNN (Convolutional Neural Network) dalam deteksi bola. Terdapat empat sudut dalam grafik: TP (True Positive), FP (False Positive), TN (True Negative), dan FN (False Negative).

Gambar menunjukkan bahwa di bagian atas kiri terdapat nilai 85, yang kemungkinan besar mewakili jumlah kejadian TP. Nilai ini mungkin merupakan akurasi model CNN dalam mendeteksi bola dengan tepat. Di bawahnya, ada label "Recall" dengan nilai sekitar 88%, menunjukkan bahwa model dapat mendeteksi bola dengan tingkat akuransi yang tinggi.

Di bagian kanan atas terdapat nilai 15, mungkin merupakan jumlah kejadian FP (False Positive), yaitu kesalahan dalam mengidentifikasi objek sebagai bola padahal sebenarnya bukan. Di bawahnya ada label "Precision" dengan nilai sekitar 97%, menunjukkan bahwa model dapat membedakan bola dari non-bola dengan tingkat akuransi yang sangat tinggi.

Di bagian bawah kiri terdapat label "F1-score" dengan nilai sekitar 91%, ini merupakan skor yang dihitung berdasarkan recall dan precision untuk memberikan gambaran lebih komprehensif tentang akurasi model. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

5. [37] AR A Besari, AA Saputra, WH Chin, N Kurnianingsih, Kubota. Hand-object interaction recognition based on visual attention using multiscopic cyber-physical-social system. (2023-07)

[38] KD Nguyen, LA Corben, PN Pathirana, MK Horne, MB Delatycki, DJ Szmulewicz. The assessment of upper limb functionality in friedreich ataxia via self-feeding activity. (2020-04)

[39] A Ganguly, G Rashidi, K Mombaur. Comparison of the performance of the leap motion controller TM with a standard marker-based motion capture system. (2021-03)

[40] C Dai, X Hu. Finger joint angle estimation based on motoneuron discharge activities. (2020-03)

[41] S Jegelka. Theory of graph neural networks: Representation and learning. (2022)

[42] M Fey, JEric Lenssen. Fast graph representation learning with PyTorch geometric. (2019)

[43] AR A Besari, WH Chin, N Kubota, Kurnianingsih. Ecological approach for object relationship extraction in elderly care robot. (2020-12)

[44] HR Nasrabadi, J.-M Alonso. Modular streaming pipeline of eye/head tracking data using Tobii pro glasses 3. (2022-09)

[45] C.-Y Wang, A Bochkovskiy, H.-Y. Mark Liao. Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. (2022)

[46] H Fu, L Wu, M Jian, Y Yang, X Wang. MF-SORT: Simple online and realtime tracking with motion features,'' in Image Graphics. (2019)

[47] F Zhang, V Bazarevsky, A Vakunov, A Tkachenka, G Sung, C.-L Chang, M Grundmann. MediaPipe hands: On-device real-time hand tracking. (2020)

[48] Q Cai, J Li, J Long. Effect of physical and virtual feedback on reach-to-grasp movements in virtual environments. (2022-06)

[49] S Shin, W Kim. Skeleton-based dynamic hand gesture recognition using a part-based GRU-RNN for gesture-based interface. (2020)

[50] EP Larsen, JM Kolman, FN Masud, F Sasangohar. Ethical considerations when using a mobile eye tracker in a patient-facing area: Lessons from an intensive care unit observational protocol. (2020-11)

[51] AR A Besari, AA Saputra, WH Chin, N Kubota, Kurnianingsih. Feature-based egocentric grasp pose classification for expanding humanobject interactions. (2021-06)

[52] MK Cain, Z Zhang, K.-H Yuan. Univariate and multivariate skewness and kurtosis for measuring nonnormality: Prevalence, influence and estimation. (2017-10)

[53] TJ Bosch, T Hanna, KA Fercho, LA Baugh. Behavioral performance and visual strategies during skill acquisition using a novel tool use motor learning task. (2018-09)

[54] M Yani, AR A Besari, N Yamada, N Kubota. Ecological-inspired system design for safety manipulation strategy in home-care robot. (2020-09)

[55] S Wang, J Zhao, C Shao, C Dong, C Yin. Truck traffic flow prediction based on LSTM and GRU methods with sampled GPS data. (2020)

[56] M Kunda, ME Banani, JM Rehg. A computational exploration of problem-solving strategies and gaze behaviors on the block design task. (2016)

[57] S Li, Y Li, Y Li, M Li, X Xu. YOLO-FIRI: Improved YOLOv5 for infrared image object detection. (2021)

[58] NA Hashim, NA A Razak, NA A Osman. Comparison of conventional and virtual reality box and blocks tests in upper limb amputees: A case-control study. (2021)

[59] J Négyesi, P Négyesi, T Hortobágyi, S Sun, J Kusuyama, RM Kiss, R Nagatomi. Handedness did not affect motor skill acquisition by the dominant hand or interlimb transfer to the non-dominant hand regardless of task complexity level. (2022-10)

[60] L Wang, J Liu, J Lan. Feature evaluation of upper limb exercise rehabilitation interactive system based on kinect. (2019)

[61] Takenori Obo (member, Ieee. he became an Assistant Professor with the Department of Mechanical Systems Engineering, Faculty of System Design, Tokyo Metropolitan University. He is currently with the Department of Mechanical Systems Engineering, Faculty of System Design, Tokyo Metropolitan University. He is a member of the Society of Instrument and Control Engineers, the Japan Society of Intelligent Information Fuzzy. (2014-04)

[62] Negeri Semarang, Indonesia. He is currently a Professor with the Department of Mechanical Systems Engineering, Graduate School of Systems Design, Tokyo Metropolitan University, Japan. His current research interests include coevolutionary computing, fuzzy computing, topological mapping, cognitive robotics, social robotics, and informationally structured space. He has published more than 500 refereed journals and conference papers in the above research fields. He received the Best Paper Award from IEEE IECON 1996 and the Best Paper Award from IEEE CIRA 1997, amongst others. (1997) (Multiscopic CPSS for Independent Block-Design Test Based on Hand–Object Interaction Recognition With Visual Attention, page 2)

6. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

7. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

8. TABLE 1. The proposed system with related works.

Tabel ini menjelaskan sistem yang diusulkan bersama dengan karya terkait dalam penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang". Tabel ini berisi 39 baris dan 9 kolom, tetapi hanya memuat informasi singkat tentang beberapa studi terkait.

Variabel/kolom utama adalah:

* Judul penelitian yang berkaitan dengan metode CNN dan kamera Zed.
* Karya-karya yang relevan yang dikemukakan sebagai referensi.
* Deskripsi singkat tentang aplikasi robot penjaga gawang dan penggunaan metode CNN.

Nilai atau pola penting dari tabel ini adalah:

* Penggunaan metode CNN untuk mendeteksi posisi bola dalam lingkungan tiga dimensi, yang merupakan kemampuan utama dari metode tersebut.
* Aplikasi robot penjaga gawang sebagai salah satu penggunaan metode CNN.

Insight singkat yang bisa dibaca manusia adalah bahwa penelitian ini berusaha mengembangkan sistem kombinasi antara kamera Zed dan metode CNN untuk mendeteksi posisi bola dengan akurasi tinggi, serta memahami pergerakan bola dalam lingkungan yang beragam. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 3)

### response

CNN (Convolutional Neural Network) adalah jenis jaringan saraf tiruan yang sangat efektif untuk menganalisis dan memproses data visual seperti gambar dan video. Dalam konteks penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang", CNN digunakan untuk memprediksi posisi bola berdasarkan data posisi yang telah dikumpulkan selama sesi pelatihan.

### reference


Tabel ini menjelaskan sistem yang diusulkan bersama dengan karya terkait dalam penelitian "Penginderaan Bola Menggunakan Metode CNN Dengan Kamera Zed pada Aplikasi Robot Penjaga Gawang". Nilai atau pola penting dari tabel ini adalah: * Penggunaan metode CNN untuk mendeteksi posisi bola dalam lingkungan tiga dimensi, yang merupakan kemampuan utama dari metode tersebut. * Aplikasi robot penjaga gawang sebagai salah satu penggunaan metode CNN. Insight singkat yang bisa dibaca manusia adalah bahwa penelitian ini berusaha mengembangkan sistem kombinasi antara kamera Zed dan metode CNN untuk mendeteksi posisi bola dengan akurasi tinggi, serta memahami pergerakan bola dalam lingkungan yang beragam. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 3)

---

## Sample 27

- conversation_id: 13
- user_chat_id: 651
- bot_chat_id: 652

### user_input

Mengapa CNN digunakan dalam deep learning?

### retrieved_context

1. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

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

2. Qurishee [71] presented an autonomous pavement condition evaluation employing deep learning, an unmanned aerial vehicle (UAV), and Raspberry Pi tiny computer technologies, which improves road maintenance and renovation management efficiency and cost effectiveness. A lowcost Raspberry Pi smart defect-detecting camera was set up with the trained SSD MobileNet v1, which can be deployed with a UAV for real-time and remote pavement condition inspection. According to preliminary data, the smart pavement detector camera achieves 60% accuracy at 1.2 frames per second on the Raspberry Pi and 96% accuracy at 13.8 frames per second on a CPU-based computer. Hassan et al. [72] employs CNN models that are improved tiny YOLO V3 on UAVs and achieves good results, with precision, sensitivity, and F1 score values better than 85%, but without considering FPS. Sathvik et al. [39] introduce

TABLE 1. Comparison of object detection models deployed on edge device.

pothole detection, an edge computing framework that runs efficient deep neural networks, lowering the latency of earlier techniques. Using transfer learning-based models, an F1 score of 0.64. The YOLO V7 model had an F1 score of 0.51, which improved proportionally (the higher the F1 score, the more efficient the training model) as the number of epochs increased. The YOLO V7 runs on a CPU-based computer, however it does not consider run on edge devices.

Several studies using CNN models deployed on NVIDIA Jetson Nano devices include the SSD-MobileNet model with a batch size of 64 and mAP of 0.22 [48], the MobileNet V2 model, and the SSD Resnet50V1 model [34], [35]. The MobileNet V2 model using hyperparameter settings has a higher mAP of 0.0869 and average recall 0.241 than the SSD Resnet50V1. Yebes et al. [40] created a massive dataset of images with pothole annotations and road scenes from many cities across the world, captured with various cameras, vehicles, and viewpoints under varying environmental circumstances. Their fine-tuned Faster R-CNN Inception v2, Faster R-CNN Resnet101, and Faster R-CNN Inception-Resnet v2 models reached precision 75%, and their CNN model deployed the pothole detector on the Nvidia DrivePX2 platform running at 5-6 frames per second. Based on the findings of this investigation, CNN models were included in the hardware, as indicated in Table 1, although further research is needed to improve system performance (mAP, AR, F1 score) and speed up inference time. Based on previous studies on road damage, several researchers have utilized the CNN model by optimizing its network structure. Specifically, the YOLO model automates the network structure through the introduction of a new module. However, few YOLOv3 models incorporate hyperparameter optimization, with only one study utilizing the Bayesian method. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 1)

3. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

4. The pooling layer, which comes after the convolution layer, is meant to combine key information and lower the dimensionality of the feature map. Max pooling, which chooses the maximum value within each condensed area of the feature map, is a frequently used kind of pooling. This lessens the number of parameters that must be computed and increases the model's resistance to slight variations in the input features' locations.

CNNs typically have multiple sets of successive convolution and pooling layers, which allow the network to detect increasingly complex features at each layer. Early layers may detect simple edges and lines, while deeper layers may detect more complex objects, such as specific shapes and patterns.

The final input is supplied into the fully connected layer after passing through several convolution and pooling layers. Every neuron in this layer is connected to every other neuron in the layer before it, enabling the network to compile the features that were taken out of the earlier levels and come to a conclusion. An activation function that aids in the final classification, such as ReLU (Rectified Linear Unit) or Softmax, typically follows this completely connected layer.

This study designs and implements appropriate parameter values in each layer of the CNN used. Previous researchers have created several methods for artificial intelligence that have been tried to be implemented on the ERSOW robot. These methods are Label Propagation, Extra Tree Classifier, Ridge Classifier, Linear SVC, Passive Aggressive Classifier, AdaBoost, Label Spreading, Nearest Centroid, GaussianNB, and Dummy Classifier (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 5)

5. Keywords: Ball position prediction, ZED camera, deep learning, convolutional neural network, ERSOW goalkeeper robot (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 1)

6. FIGURE 6. CNN block diagram.

Gambar ini menampilkan skema blok CNN (Convolutional Neural Network). Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar. Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi).

Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. Namun, detail tentang jenis citra yang digunakan sebagai input masih tidak dapat diidentifikasi secara pasti dari gambar ini.

Dari skema blok CNN ini, dapat disimpulkan bahwa proses pemrosesan gambar dilakukan melalui beberapa tahap konvolusi dan downsampling dengan maksimum. Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori.

Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Oleh karena itu, interpretasi harus berfokus pada gambaran umum proses yang terjadi dalam CNN daripada detil teknis parametris. (Development of a Speech Emotion Recognition Dataset for Indonesian, page 6)

7. This research uses the ROS system because it has the ability to integrate camera sensors with artificial intelligence methods and several other combined sensors in the robot. Fig. 4 shows the basic communication system for accessing the ZED camera on the robot. Image information is acquired over time and processed in real-time.  The prediction system that has been created using the CNN algorithm tries to change the layer parameter model to get the best results in classifying the position of the predicted direction of the ball. The dataset was collected as shown in Fig. 6. The CNN design used is as in Fig. 7 and equations ( 4) to (9). Convolutional Neural Network (CNN) is a type of artificial neural network specifically designed to process two-dimensional grid-shaped data, such as images. The convolution layer, pooling layer, and fully connected layer are the three primary hierarchical layers of a CNN. The central component of a CNN is the convolution layer, where different visual elements like edges, textures, and patterns are detected by applying filters or kernels to the input. A feature map reflecting the position of a certain feature in the original image is produced by the convolution layer's filters scanning the entire input. The way that neurons in the human brain react to visual stimuli is comparable to this mechanism. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 4)

8. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

### response

CNN (Convolutional Neural Network) digunakan dalam deep learning karena dapat memproses data dua dimensi, seperti citra dan video, dengan efisiensi tinggi. CNN memiliki struktur hierarkis yang terdiri dari lapisan konvolusi, pooling, dan fully connected, yang memungkinkannya untuk mendeteksi fitur-fitur visual dalam citra.

Dalam konteks penelitian ini, CNN digunakan untuk memprediksi posisi bola menggunakan kamera ZED. CNN dapat mengambil citra dari kamera dan menghasilkan klasifikasi pada posisi bola dengan akurasi tinggi.

CNN juga digunakan dalam beberapa penelitian lainnya, seperti deteksi kerusakan jalan, pengenalan emosi suara, dan pengenalan objek. Dalam semua kasus, CNN dapat memproses data visual dengan efisiensi tinggi dan menghasilkan hasil yang akurat.

Dalam konteks ini, CNN digunakan karena kemampuannya untuk:

1. Memproses citra dua dimensi
2. Mendeteksi fitur-fitur visual
3. Menghasilkan klasifikasi pada posisi bola dengan akurasi tinggi

Jadi, CNN digunakan dalam deep learning karena dapat memproses data visual dengan efisiensi tinggi dan menghasilkan hasil yang akurat.

### reference


Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori. Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos.

---

## Sample 28

- conversation_id: 13
- user_chat_id: 653
- bot_chat_id: 654

### user_input

Bagaimana CNN bekerja secara sederhana?

### retrieved_context

1. FIGURE 6. CNN block diagram.

Gambar ini menampilkan skema blok CNN (Convolutional Neural Network). Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar. Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi).

Pada bagian atas skema, terdapat label "Input" dan "Output", yang menunjukkan bahwa gambar ini berfungsi untuk menerima input suatu citra dan menghasilkan output berupa hasil pengenalan atau klasifikasi. Namun, detail tentang jenis citra yang digunakan sebagai input masih tidak dapat diidentifikasi secara pasti dari gambar ini.

Dari skema blok CNN ini, dapat disimpulkan bahwa proses pemrosesan gambar dilakukan melalui beberapa tahap konvolusi dan downsampling dengan maksimum. Fungsi utamanya adalah untuk mengekstrak fitur-fitur penting dalam citra dan menghasilkan klasifikasi yang akurat terhadap suatu tipe objek atau kategori.

Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Oleh karena itu, interpretasi harus berfokus pada gambaran umum proses yang terjadi dalam CNN daripada detil teknis parametris. (Development of a Speech Emotion Recognition Dataset for Indonesian, page 6)

2. The Convolutional Neural Network (CNN) model is trained using the prepared dataset. CNN is a type of deep neural network that is highly effective for the analysis and processing of visual data such as images and videos. In this context, CNN is used to predict the position of the ball based on the position data that has been collected during the training session. The training process involves adjusting the weights of the model through the backpropagation technique to minimize the prediction error. The Fig. 7 is a sequential model of the CNN architecture for ball position prediction. A sequential model is a series of layers that are processed sequentially from input to output. The given model consists of several types of layers: Conv1D, AveragePooling1D, Dropout, MaxPooling1D, Flatten, and Dense. The operation process is in equations ( 4) to (9). (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 7)

3. Here is the complete sequence of transformations that occur to the input signal as it passes through each layer in the model: 1. Conv1D 1:

• Input: (None, 10, 512)

• Output: (None, 10, 512)

• Convolution operation with a certain filter size. 2. AveragePooling1D 1:

• Input: (None, 10, 512)

• Output: (None, 5, 512)

• Takes the average of every two consecutive values, halving the length of the signal. The model takes an input signal, operates it through multiple layers of convolution, pooling, dropout, and finally dense layers to produce the output. Each layer has specific functions that help in extracting important features from the signal and finally make predictions based on those features.

To train the CNN, a loss function is used which measures the difference between the model's prediction and the true value. The loss function used is the Mean Squared Error (MSE), which can be expressed by the following formula:

where:

• ŷi is the model prediction for the i-th sample,

• y i is the actual value for the i-th sample,

• N is total number of samples in the dataset.

During the training phase, the model weights are updated using the average square of the difference between the predicted and actual values, which is computed using this loss function. By minimizing this loss value, the CNN model is expected to improve its prediction accuracy of the ball position. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 8)

4. The road damage detection research makes use of laser sensors to rebuild 3D road damage as well as stereo vision technologies. Several sensors are required for the stereo vision system, including two cameras, an LED, a laser, and LiDAR. The laser sensor has a small beamwidth; thus, it cannot detect road damage in the form of a large hole, necessitating the use of an array of LEDs, lasers, LiDARs, and other sensors [18], [49]. Reconstructing the pothole takes time, whether using an LED array, laser, or LiDAR. Furthermore, 3D road defect reconstruction and stereo vision require well-lit lighting and slow vehicle speeds [17], [18], [50].

Further research used image-processing techniques. Potholes are a form of road irregularity that can be recognized with traditional image processing techniques. To achieve high accuracy, this technique takes numerous steps, including manual image feature extraction and image processing parameter adjustments. As a result, the image frame rate varies depending on traffic circumstances [21]. Some research that investigated road conditions, pavement conditions, potholes, cracks, smart phone sensors, and accelerometers used machine learning techniques such as support vector machines, neural networks, multilayer perceptron, and decision trees [16]. Furthermore, research is being conducted to detect pavement damage using ML algorithms such as support vector machines, artificial neural networks, and random forests [51]. To improve accuracy, ML models require significant computer resources during data processing, which also includes manual feature analysis.

Several studies used deep convolutional neural network (CNN) techniques to automate the simultaneous feature extraction and categorization of objects [41], [52]. This is challenging to incorporate into real-time road defect detection systems. The deployment of CNN models for road damage detection on devices requires a balance between high accuracy and high efficiency [53]. The use of CNN models for road damage detection on devices requires achieving a balance between high accuracy and high efficiency. The use of CNN models for road damage detection on devices necessitates striking a balance between high accuracy and high efficiency. The parameter system performance deployment model CNN on devices performs well in terms of precision, recall, F1-score, and as well as efficiency of time inference.

The CNN models perform exceptionally well in terms of high accuracy, precision, recall, and low loss. This requires CNN models with large architecture and competitive computing costs that are inefficient. To do this while maintaining high accuracy, a simplified CNN model configuration setting is required to achieve good CNN model system performance. High efficiency, which is the CNN model system performance, enables it to detect road faults on edge devices with a short inference time. Because the CNN model on edge devices have limited storage capacity, inference time must be considered. Taking this into account, the CNN model offers good system performance and a short inference time for simpler model configurations, but high accuracy is difficult to achieve. To obtain optimal system performance, the CNN model parameters must be properly chosen. When selecting a detection model, there is no definitive answer as to which model has the best performance [31], [53].

Improving system performance in computer vision, object recognition, and classification using CNN models can be achieved through various methods. These include modifying or adding components to the CNN model structure and optimizing hyperparameter selection during CNN model training. The strategy of enhancing the CNN structure aims to improve feature extraction efficiency and model accuracy by modifying or incorporating new components into the CNN architecture. Several studies have focused on enhancing CNN models by modifying or adding components to the existing CNN structure [54], [55], [56], [57], [58], [59]. DenseNet was integrated into the YOLOv4 backbone to optimize feature transfer and reuse. This involved several modifications, such as adjusting the Path Aggregation Network (PANet) [54], introducing New Residual Blocks, applying Spatial Pyramid Pooling (SPP), modifying the PANet, and utilizing Hard-Swish activation functions [59]. Similarly, researchers have integrated DenseNet blocks into the YOLOv5 backbone to enhance the preservation and reuse of critical feature information. This was achieved by incorporating a Convolutional Block Attention Module (CBAM) [56]. Another study introduced a novel framework called Multiple Graph Learning Neural Networks (MGLNN) for semi-supervised learning on graph-based data [55]. Additionally, modifications were made to the YOLO model using the CSPDarknet53 backbone structure, which included Residual Blocks, DenseNet, Spatial Pyramid Pooling (SPP), and the Path Aggregation Network (PANet) [57]. (iYOLOV7-TPE-SS: Leveraging Improved YOLO Model With Multilevel Hyperparameter Optimization for Road Damage Detection on Edge Devices, page 2)

5. [38] C Cavina-Pratesi, C Hesse. Why do the eyes prefer the index finger? Simultaneous recording of eye and hand movements during precision grasping. (2013-04)

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

6. • Function: Converts multi-dimensional signals into onedimensional (1D) signals.

• Output: 1D signal. 6. Dense (Fully Connected) layer

• Function: Linearly combine all the signal features and apply an activation function.

• Operation:

where x is the input, σ is the activation function, w is the weight matrix, and b is the bias vector.

• Output: The signal that has been transformed by the dense layer. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 1)

7. FIGURE 9. CNN model training result.

Gambar ini menampilkan grafik hasil pelatihan model CNN (Convolutional Neural Network). Grafik ini terlihat seperti garis di atas yang menunjukkan proses pengembangan akurasi model CNN selama proses pelatihan. Pada awalnya, akurasi model cukup rendah, tetapi kemudian meningkat secara signifikan seiring dengan berjalannya waktu dan iterasi pelatihan.

Pada grafik tersebut terdapat beberapa titik tertentu yang menunjukkan peningkatan drastis dalam akurasi. Meskipun tidak ada angka spesifik yang dapat diidentifikasi, namun jelas bahwa model CNN telah berhasil meningkatkan akurasinya hingga mencapai nilai yang sangat tinggi.

Dari grafik ini kita dapat menyimpulkan bahwa proses pelatihan model CNN telah berjalan dengan efektif dan akurasi model meningkat secara signifikan. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 10)

8. This research uses the ROS system because it has the ability to integrate camera sensors with artificial intelligence methods and several other combined sensors in the robot. Fig. 4 shows the basic communication system for accessing the ZED camera on the robot. Image information is acquired over time and processed in real-time.  The prediction system that has been created using the CNN algorithm tries to change the layer parameter model to get the best results in classifying the position of the predicted direction of the ball. The dataset was collected as shown in Fig. 6. The CNN design used is as in Fig. 7 and equations ( 4) to (9). Convolutional Neural Network (CNN) is a type of artificial neural network specifically designed to process two-dimensional grid-shaped data, such as images. The convolution layer, pooling layer, and fully connected layer are the three primary hierarchical layers of a CNN. The central component of a CNN is the convolution layer, where different visual elements like edges, textures, and patterns are detected by applying filters or kernels to the input. A feature map reflecting the position of a certain feature in the original image is produced by the convolution layer's filters scanning the entire input. The way that neurons in the human brain react to visual stimuli is comparable to this mechanism. (Prediction of Ball Position Using CNN Methods With Zed Camera on Goalkeeper Robot Application, page 4)

### response

CNN (Convolutional Neural Network) bekerja dengan beberapa lapisan utama, yaitu:

1.  Lapisan Konvolusi (Convolution Layer): Mencari fitur-fitur visual seperti garis-garis, tekstur-teksur, dan pola-polaa dalam citra input dengan menggunakan filter atau kernel.
2.  Lapisan Pooling (Pooling Layer): Mengurangi dimensi dari feature map yang dihasilkan oleh lapisan konvolusi untuk menghemat jumlah parameter yang perlu diproses.
3.  Lapisan Fully Connected (Fully Connected Layer): Menggabungkan semua fitur-fitur yang telah ditemukan sebelumnya untuk membuat prediksi.

CNN bekerja dengan cara memproses citra-citra input secara sequential, yaitu:

1.  Citra input diproses oleh lapisan konvolusi untuk menemukan fitur-fitur visual.
2.  Fitur-fitur yang ditemukan kemudian diolah oleh lapisan pooling untuk menghemat jumlah parameter.
3.  Lalu hasilnya dikirim ke lapisan fully connected untuk membuat prediksi.

Dengan cara ini, CNN dapat menemukan fitur-fitur yang relevan dalam citra-citra input dan membuat prediksi yang akurat.

### reference


Lapisan-lapisan tersebut terlihat seperti kotak-kotak persegi panjang yang berurutan, masing-masing memiliki label yang menunjukkan jenis operasi yang dilakukan: Conv2D (lapisan konvolusi), MaxPooling2D (proses downsampling dengan memilih maksimum nilai), Flatten (mengubah pola input 3 dimensi menjadi array satu dimensi). Perlu diingat bahwa karena hanya ada skema blok saja, detail tentang parameter atau nilai spesifik dari setiap lapisan konvolusi tidak dapat dilihat. Elemen visual utama adalah beberapa lapisan konvolusi yang dihubungkan dengan satu sama lain melalui proses pemrosesan suatu gambar.

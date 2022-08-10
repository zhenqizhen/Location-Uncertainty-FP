# Location-Uncertainty-FP
1.draw_traj
---Click the run button to get
	---The database generates trajectories 1-8 and test trajectories 1-2, as shown in Figure 3
2.Create_database_heatmap
---Click the run button to get
	---Reference database and I-A database AP 6 RSS heat map, as shown in Figure 6
	---The statistical table of LF difference between I-A, I-B database and reference database RP point, as shown in Table I
3.positioning_statistics
---Click the run button to get
	---Positioning results of various strategies, statistical values Positioning error CDF and table of various strategies，WiFi positioning errors, positioning difference and weighted
	---Positioning results of various strategies, Strategy 0, I-A, I-B, I-C, as shown in Figure 7
	---Positioning results of various strategies, Strategy 0, II-A1, II-A2, II-A3, II-C1, II-C2, II-C3, as shown in Figure 10
	---Positioning error CDF of various strategies, Strategy 0, I-A, I-B, I-C, as shown in Figure 8
                ---Positioning error CDF of various strategies, Strategy 0, II-A1, II-A2, II-A3, II-C1, II-C2, II-C3，as shown in Figure11
	---Statistical value of positioning errors, Strategy 0, I-A, I-B, I-C, as shown in Table II
                ---Statistical value of positioning errors, Strategy 0, II-A1, II-A2, II-A3, II-C1, II-C2, II-C3，as shown in Table IV
	---I-B, I-C positioning difference, weight and location unceratinty, as shown in Table III
4.Demo_Create_Database
---exe file, through this software, the data_for_db.txt corresponding to the fingerprint situation can be generated into the corresponding final.txt file, 
     where 0 means that the location uncertainty is not considered, and 1 means that the location uncertainty is considered.
---Click the Demo_Create_Database.exe file,
     select different data_for_db.txt according to the different fingerprints of the experiment file in the \Demo\data\data_for_db&Database_final file, 
     select the ap_wifi.txt file although in the \Demo\data\data_for_db&Database_final file
     select the database output path in the interface, which is the location of the final.txt file.
     When generating the database sonsidering the influence of location uncertainty, and the value of Num in the interface is set to 0. 
      If generating the database not sonsidering the influence of location uncertainty , the value of Num in the interface is set to 1
      click the Create_database(final.txt) button completes the output of the database of the required data.

5.data
---The data used in this experiment
	<1>.traj
	 ---the database generates trajectories 1-8 and test trajectories 1-2, as shown in Figure 3
	 a.database_traj：
        	 ---.DAT file, database generation trajectories, File Format, time, latitude, lotitude, height 
    	 b. test_traj
       	 ---.DAT file, test trajectories, File Format, time, latitude, lotitude, height 
                 ---.txt, test data. file format, time, latitude, lotitude, RSS15 
	<2>.data_for_db&Database_final
	 ---It mainly includes the data_for_db.txt file of the aggregated fingerprints and the database final.txt file of the corresponding fingerprints. 
	      The types and numbers of different fingerprints are also different according to different environments.
	 ---data_for_db.txt, File Format, identification, time, latitude, longitude, elevation, uncertainty, 0, 0, 0, RSS15 values
 	 ---final, File Format,  Latitude, longitude, gridid, elevation, uncertainty, RSS15 values, the reference uncertainty is 0, does not consider the uncertainty, its value is also 0

	a. robot_huamn_crowdsourcing_semantics：
       	 ---A moderate amount of professional fingerprints (robort traj 1-4 and Professional human traj 1-4) and Dense ubiquitous data (Crowdsourcing traj 1-8 and Semantics wifi ap location)
       	 ---Reference Strategy 0 final.txt and covered fingerprint data data_for_db.txt
     	 ---average Strategy I-A final.txt and covered fingerprint data data_for_db.txt
	 ---Weighted_average Strategy I-B，I-C final.txt and covered fingerprint data data_for_db.txt
	b. robot12_huamn12
	  ---Sparse professional fingerprints, robot traj 1 and 2, Professional human traj 1 and 2
        	  ---average Strategy II-A1 final.txt and covered fingerprint data data_for_db.txt
      	  ---Weighted_average Strategy II-C1 final.txt and covered fingerprint data data_for_db.txt
	c. crowdsourcing_semantics
       	  ---Dense Crowdsourced Semantic Ubiquitous Fingerprints,  Crowdsourcing traj 1-8 and Semantics wifi ap location
       	  ---average Strategy II-A2 final.txt and covered fingerprint data data_for_db.txt
       	  ---Weighted_average Strategy II-C2 final.txt and covered fingerprint data data_for_db.txt
	d. robot12_human12_crowdsourcing_semantics
       	  ---Sparse professional fingerprints, robot traj 1 and 2, Professional human traj 1 and 2 ,and Dense Crowdsourced Semantic Ubiquitous Fingerprints,  Crowdsourcing traj 1-8 and Semantics wifi ap location
        	  ---average Strategy II-A3 final.txt and covered fingerprint data data_for_db.txt
       	  ---Weighted_average Strategy II-C3 final.txt and covered fingerprint data data_for_db.txt
	e. ap_wifi.txt：
       	  ---The point coordinates of the WiFi AP point in Figure 3(a) and the parameters used to calculate the RSS using the WiFi wireless signal transmission attenuation equation
       	  ---File Format: label, latitude, longitude, elevation, b, n, MAC address






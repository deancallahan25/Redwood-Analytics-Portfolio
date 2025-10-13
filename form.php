<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<!--
    by: Redwood Analytics
    last modified: 10/03/25

    you can run this using the URL: https://nrs-projects.humboldt.edu/~dpc43/311project/form.php

-->
<head>
    <title> Waste Audit Form </title>
    <meta charset="utf-8" />
    <?php
    ini_set('display_errors',1);
    error_reporting(E_ALL);
    require_once("hum_conn_no_login.php");
    ?>

</head>
<body>
    <h1>Cal Poly Humboldt Waste Audit Form V1.0</h1>
    <p> By Redwood Analytics</p>
   
    <?php
    if ($_SERVER["REQUEST_METHOD"]=="GET")
    {    
    ?>
      <form method="POST" action="<?= htmlentities($_SERVER["PHP_SELF"], ENT_QUOTES) ?>">
    <label for="building_info">What building did you conduct the audit on? </label>
     <select name="building_info" id= "building_info">

    <?php

    $conn = hum_conn_no_login();
   
    $building_query_str = "select building_id, building_name
                        from building
                        order by building_name";

    $building_stmt = oci_parse($conn, $building_query_str);

    oci_execute($building_stmt, OCI_DEFAULT);
 while(oci_fetch($building_stmt))
    {
            $curr_building_id = oci_result($building_stmt, 1);
            $curr_building_name = oci_result($building_stmt, 2);
    ?>

        
        <option value="<?=$curr_building_id ?>"> <?=$curr_building_name ?> - <?=$curr_building_id ?> </option>
<?php }
        oci_free_statement($building_stmt);
        oci_close($conn);
?>
    </select>
    <br /> 
    <br />
    <label for="landfill_weight">Landfill Weight (lbs):</label>
    <input type="number" id="landfill_weight" name="landfill_weight" min="0.0" required="required"/>
    <label for="landfill_volume">Landfill Volume (%):</label>
    <input type="number" id="landfill_volume" name="landfill_volume" min="0.0" max="100" required="required"/>
     <br />

     <br />
    <label for="mixed_recycling_weight">Mixed Recycling Weight (lbs):</label>
    <input type="number" id="mixed_recycling_weight" name="mixed_recycling_weight" min="0.0" required="required"/>
    <label for="mixed_recycling_volume">Mixed Recycling Volume (%):</label>
    <input type="number" id="mixed_recycling_volume" name="mixed_recycling_volume" min="0.0" max="100" required="required"/>

    <br />
     

    <br />
    <label for="compost_weight">Compost Weight (lbs):</label>
    <input type="number" id="compost_weight" name="compost_weight" min="0.0" required="required"/>
    <label for="compost_volume">Compost Volume (%):</label>
    <input type="number" id="compost_volume" name="compost_volume" min="0.0" max="100" required="required"/>
    <br />

     <br />
    <label for="universal_waste_recycling_weight">Universal Waste Recycling Weight (lbs):</label>
    <input type="number" id="universal_waste_recycling_weight" name="universal_waste_recycling_weight" min="0.0" required="required"/>
    <label for="universal_waste_recycling_volume">Universal Waste Recycling Volume (%):</label>
    <input type="number" id="universal_waste_recycling_volume" name="universal_waste_recycling_volume" min="0.0" max="100" required="required"/>    
<br />

    <br />
    <label for="hazardous_waste_weight">Hazardous Waste Weight (lbs):</label>
    <input type="number" id="hazardous_waste_weight" name="hazardous_waste_weight" min="0.0" required="required"/>
    <label for="hazardous_waste_volume">Hazardous Waste Volume (%):</label>
    <input type="number" id="hazardous_waste_volume" name="hazardous_waste_volume" min="0.0" max="100" required="required"/>
    <br />

    <br />
    <label for="other_weight">Other Weight (lbs):</label>
    <input type="number" id="other_weight" name="other_weight" min="0.0" required="required"/>
    <label for="other_volume">Other Volume (%):</label>
    <input type="number" id="other_volume" name="other_volume" min="0.0" max="100" required="required"/>

    <br />

    <br />
    <label for="toxic_items_comment">What are the most toxic items found?</label>
    <br />
    <textarea id="toxic_items_comment" name="toxic_items_comment" rows="3" cols="35"></textarea>
    <br />
    



    <br />
    <label for="collection_methods_comment">Did you notice anything about the garbage collection systems in the building? (e.g., had dedicated paper towel bins in bathroom, had e-waste bin) </label>
    <br />
    <textarea id="collection_methods_comment" name="collection_methods_comment" rows="3" cols="35"></textarea>
    <br />


    <br />
    <label for="other_comment">In general, do you have any recommendations about anything? </label>
    <br />
    <textarea id="other_comment" name="other_comment" rows="3" cols="35"></textarea>
    <br />

    <br />
    <label for="audit_date">Date:</label>
    <input type="date" id="audit_date" name="audit_date" required="required">
    <br />
    
    <br />
    <label for="audit_time">Time:</label>
    <input type="time" id="audit_time" name="audit_time" required="required">
    <br />
    
    <br />
    <label for="auditor_email">Email:</label>
    <input type="email" id="auditor_email" name="auditor_email" required="required">
    <br />

    <br />
    <label for="auditor_fname">First Name:</label>
    <input type="text" id="auditor_fname" name="auditor_fname">
    <label for="auditor_fname">Last Name:</label>
    <input type="text" id="auditor_lname" name="auditor_lname">

    <br />

     
    <br />
    <p> Optionally fill these in to improve the quality of the data collection:</p>
    <label for="bags_audited">Number of Bags Audited:</label>
    <input type="number" id="bags_audited" name="bags_audited">
      <label for="total_weight">Your calculated total weight:</label>
    <input type="number" id="total_weight" name="total_weight">
    <br />



    <br /> 
    <input type="submit"/>
    </form>

<?php }
    else
    {
	    $building_id=$_POST["building_info"];
	    $landfill_weight=$_POST["landfill_weight"];
	    $landfill_volume=$_POST["landfill_volume"];
	    $mixed_recycling_weight=$_POST["mixed_recycling_weight"];
	    $mixed_recycling_volume=$_POST["mixed_recycling_volume"];
            $compost_weight=$_POST["compost_weight"];
	    $compost_volume=$_POST["compost_volume"];
	    $universal_waste_recycling_weight=$_POST["universal_waste_recycling_weight"];
	    $universal_waste_recycling_volume=$_POST["universal_waste_recycling_volume"];
	    $hazardous_waste_weight=$_POST["hazardous_waste_weight"];
	    $hazardous_waste_volume=$_POST["hazardous_waste_volume"];
	    $other_weight=$_POST["other_weight"];
	    $other_volume=$_POST["other_volume"];
	    $toxic_materials_comment=$_POST["toxic_items_comment"];
	    $collection_methods_comment=$_POST["collection_methods_comment"];
	    $other_comment=$_POST["other_comment"];
	    $audit_date=$_POST["audit_date"];
	    $audit_time=$_POST["audit_time"];
	    $auditor_email=$_POST["auditor_email"];
            $auditor_fname=$_POST["auditor_fname"];
	    $auditor_lname=$_POST["auditor_lname"];
	    $total_weight=$_POST["total_weight"];
	    $bags_audited=$_POST["bags_audited"];


	    $conn=hum_conn_no_login();
	    $auditor_insert_str="INSERT INTO Auditors (auditor_id, email_address, auditor_fname, auditor_lname)
		                 VALUES (NULL,:email, :fname, :lname)";
		
	    $auditor_insert_stmt=oci_parse($conn, $auditor_insert_str);
	    oci_bind_by_name($auditor_insert_stmt, ":email",$auditor_email);
	    oci_bind_by_name($auditor_insert_stmt, ":fname",$auditor_fname);
  	    oci_bind_by_name($auditor_insert_stmt, ":lname",$auditor_lname);
	    oci_execute($auditor_insert_stmt, OCI_DEFAULT); 



	    $audit_insert_str="INSERT INTO Waste_Audit (audit_id, building_id, number_bags, date_conducted,total_weight)
				VALUES (NULL, :building, :num_bags,TO_DATE(:audit_date,'YYYY-MM-DD'), :total_weight)";
	    $audit_insert_stmt=oci_parse($conn, $audit_insert_str);
	    oci_bind_by_name($audit_insert_stmt, ":building",$building_id);	
	    oci_bind_by_name($audit_insert_stmt, ":num_bags",$bags_audited);
	    oci_bind_by_name($audit_insert_stmt, ":audit_date",$audit_date);
	    oci_bind_by_name($audit_insert_stmt, ":total_weight",$total_weight);
 	    oci_execute($audit_insert_stmt, OCI_DEFAULT);  

            $curr_audit_id="SELECT waste_audit_seq.CURRVAL FROM dual";
     	    $audit_id_stmt=oci_parse($conn, $curr_audit_id);
	    oci_execute($audit_id_stmt);
	    $row=oci_fetch_array($audit_id_stmt);
	    $audit_id=$row[0];
	    oci_free_statement($audit_id_stmt);
	     

	    $categories=[
		["Landfill",$landfill_weight, $landfill_volume],
		["Mixed Recycling",$mixed_recycling_weight, $mixed_recycling_volume],
		["Compost",$compost_weight, $compost_volume],
		["Universal Waste Recycling",$universal_waste_recycling_weight, $universal_waste_recycling_volume],
		["Hazardous Waste",$hazardous_waste_weight, $hazardous_waste_volume],
		["Other",$other_weight, $other_volume]];
	    

	    $category_insert_str="INSERT INTO Categories(category_name, audit_id, category_weight, percent_by_weight, percent_by_volume) 
				    VALUES (:name, :audit_id, :weight,:weight_percent, :volume_percent)";
	    $category_insert_stmt=oci_parse($conn, $category_insert_str);

	    foreach ($categories as $category) {
		$category_name=$category[0];
		$category_weight=$category[1];
		$category_volume=$category[2];
		
		if ($total_weight>0){
			$category_percent_weight=round(($category_weight/$total_weight) * 100, 2);
		}
		else{
			$category_percent_weight=NULL;
		}

		oci_bind_by_name($category_insert_stmt,":name",$category_name);
		oci_bind_by_name($category_insert_stmt, ":audit_id", $audit_id);
	   	oci_bind_by_name($category_insert_stmt,":weight",$category_weight);
		oci_bind_by_name($category_insert_stmt,":weight_percent",$category_percent_weight);
		oci_bind_by_name($category_insert_stmt,":volume_percent",$category_volume);
		oci_execute($category_insert_stmt, OCI_DEFAULT);
	    }  	    

	    $comments=[
		["Toxic Material", "Comments_Toxic_Material", "toxic_items", $toxic_materials_comment],
	        ["Collection Methods", "Comments_Collection_Methods", "collection_methods", $collection_methods_comment],
        	["Other", "Comments_Other", "other_comment", $other_comment]];
	    
	    foreach ($comments as $comment){
		    $comment_type=$comment[0];
		    $comment_table=$comment[1];
		    $comment_col=$comment[2];
		    $comment_text=$comment[3];
		    
		    if(trim($comment_text)!=""){
		  
		    	$comment_insert_str = "INSERT INTO Comments (comment_id, comment_type, audit_id)
				      VALUES (NULL,:type, :audit_id)";
		        $comment_insert_stmt = oci_parse($conn, $comment_insert_str);
		        oci_bind_by_name($comment_insert_stmt, ":type",$comment_type);
			oci_bind_by_name($comment_insert_stmt,":audit_id",$audit_id);
			oci_execute($comment_insert_stmt, OCI_DEFAULT);

			$get_comment_id="SELECT comment_seq.CURRVAL FROM dual";
			$get_comment_id_stmt=oci_parse($conn, $get_comment_id);
			oci_execute($get_comment_id_stmt,OCI_DEFAULT);
			$row=oci_fetch_array($get_comment_id_stmt);
			$comment_id=$row[0];
			oci_free_statement($get_comment_id_stmt);

			$comment_type_insert="INSERT INTO {$comment_table} (comment_id,{$comment_col})
					      VALUES (:id,:text)";
			$comment_type_stmt= oci_parse($conn, $comment_type_insert);
			oci_bind_by_name($comment_type_stmt, ":id",$comment_id);
			oci_bind_by_name($comment_type_stmt,":text",$comment_text);
			oci_execute($comment_type_stmt,OCI_DEFAULT);
			oci_free_statement($comment_insert_stmt);
			oci_free_statement($comment_type_stmt);
		    }
	    }


	    

            oci_free_statement($auditor_insert_stmt);
	    oci_free_statement($audit_insert_stmt);
	    oci_free_statement($category_insert_stmt);
	    oci_commit($conn);
	    oci_close($conn);
	?>  <p> <a href="<?= htmlentities($_SERVER["PHP_SELF"], ENT_QUOTES) ?>">
	Make a new waste audit </a> </p>
	<?php

    }
   
?> 
    <footer>
    <p> Waste Audit Form </p>
    <hr />
    <p>
        Validate by pasting .xhtml copy's URL into<br />
        <a href="https://validator.w3.org/nu">
            https://validator.w3.org/nu
        </a>
        or
        <a href="https://html5.validator.nu/">
            https://html5.validator.nu/
        </a>
    </p>
    </footer>
</body>
</html>

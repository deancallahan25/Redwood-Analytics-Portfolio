<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<!--
    by: Redwood Analytics
    last modified: 10/03/25

    you can run this using the URL: https://nrs-projects.humboldt.edu/~dpc43/311project/show_results.php
-->

<head>
    <title> Waste Audit Results </title>
    <meta charset="utf-8" />
    <?php
    ini_set('display_errors',1);
    error_reporting(E_ALL);
    require_once("hum_conn_no_login.php");
    ?>
</head>

<body>
    <h1>Cal Poly Humboldt Waste Audit Results</h1>
    <p> By Redwood Analytics</p>

<?php
    $conn=hum_conn_no_login();
    $audit_list_stmt = oci_parse($conn, "
      SELECT w.audit_id, b.building_name, TO_CHAR(w.date_conducted, 'YYYY-MM-DD') AS date_conducted
      FROM Waste_Audit w, Building b
      where w.building_id = b.building_id
      ORDER BY w.audit_id");
    oci_execute($audit_list_stmt);
    $audits = [];
    while ($a = oci_fetch_assoc($audit_list_stmt)){
    	$audits[]=$a;
    }

    $selected_audit=$_GET['audit_id'] ?? null;
    $selected_audit_two=$_GET['audit_id_two'] ?? null;
    $query_stmt=null;
    $query_stmt_two=null;
    
    if ($selected_audit){
    $query_str="SELECT w.audit_id, b.building_name,w.date_conducted, c.category_name, c.category_weight, c.percent_by_weight, c.percent_by_volume
	    FROM Waste_Audit w, Building b, Categories c
	    WHERE w.building_id=b.building_id and w.audit_id=c.audit_id and w.audit_id = :audit_id
	    ORDER BY w.audit_id, c.category_name";
	    $query_stmt=oci_parse($conn, $query_str);
	    oci_bind_by_name($query_stmt, ":audit_id",$selected_audit);
            oci_execute($query_stmt);
    }

   
    if ($selected_audit_two){
    $query_str_two="SELECT w.audit_id, b.building_name,w.date_conducted, c.category_name, c.category_weight, c.percent_by_weight, c.percent_by_volume
            FROM Waste_Audit w, Building b, Categories c
            WHERE w.building_id=b.building_id and w.audit_id=c.audit_id and w.audit_id = :audit_id_two
            ORDER BY w.audit_id, c.category_name";
            $query_stmt_two=oci_parse($conn, $query_str_two);
            oci_bind_by_name($query_stmt_two, ":audit_id_two",$selected_audit_two);
            oci_execute($query_stmt_two);
    }

    





?>

<form method="get">
   <label for="audit_id"><strong>Select an Audit:</strong></label>
   <select name="audit_id" id="audit_id" required="required">
     <option value="">Choose an Audit</option>
        <?php foreach ($audits as $audit):
     		$id = htmlspecialchars($audit['AUDIT_ID']);
    		$label = htmlspecialchars($audit['BUILDING_NAME']) . " (" . htmlspecialchars($audit['DATE_CONDUCTED']) . ")";  
    		$selected=($selected_audit==$id) ? "selected" : ""; ?>
    <option value="<?= $id?>" <?= $selected ?>><?= $label?> </option> 
   <?php endforeach;?>
    </select>

   <label for="audit_id_two"><strong>Select Audit 2 (Optional):</strong></label>
   <select name="audit_id_two" id="audit_id_two">
     <option value="">Choose a Second Audit</option>
     <?php foreach ($audits as $audit):
         $id_two = htmlspecialchars($audit['AUDIT_ID']);
         $label_two = htmlspecialchars($audit['BUILDING_NAME']) . " (" . htmlspecialchars($audit['DATE_CONDUCTED']) . ")";

         $selected_two=($selected_audit_two==$id_two) ? "selected" : ""; ?>
       <option value="<?= $id_two?>" <?= $selected_two ?>><?= $label_two?> </option> 
   <?php endforeach;?>
     </select>

     <button type="submit">View Results</button>
</form>


<?php if ( $query_stmt || $query_stmt_two): ?>

<table border="1" cellpadding="5">
    <tr>
      <th>Audit ID</th>
      <th>Building</th>
      <th>Date Conducted</th>
      <th>Category</th>
      <th>Weight (lbs)</th>
      <th>% by Weight</th>
      <th>% by Volume</th>
    </tr>

<?php
if ($query_stmt){
    while ($row=oci_fetch_assoc($query_stmt)){
?>
    <tr>
        <td><?= htmlspecialchars($row['AUDIT_ID']) ?></td>
        <td><?= htmlspecialchars($row['BUILDING_NAME']) ?></td>
        <td><?= htmlspecialchars($row['DATE_CONDUCTED']) ?></td>
        <td><?= htmlspecialchars($row['CATEGORY_NAME']) ?></td>
        <td><?= htmlspecialchars($row['CATEGORY_WEIGHT']) ?></td>
        <td><?= htmlspecialchars($row['PERCENT_BY_WEIGHT'] ??'') ?></td>
        <td><?= htmlspecialchars($row['PERCENT_BY_VOLUME']) ?></td>
      </tr>
<?php
    }
}

?>
<?php if ($query_stmt_two){ ?>

<?php
    while ($row2=oci_fetch_assoc($query_stmt_two)){
?>
    <tr>
        <td><?= htmlspecialchars($row2['AUDIT_ID']) ?></td>
        <td><?= htmlspecialchars($row2['BUILDING_NAME']) ?></td>
        <td><?= htmlspecialchars($row2['DATE_CONDUCTED']) ?></td>
        <td><?= htmlspecialchars($row2['CATEGORY_NAME']) ?></td>
        <td><?= htmlspecialchars($row2['CATEGORY_WEIGHT']) ?></td>
        <td><?= htmlspecialchars($row2['PERCENT_BY_WEIGHT'] ??'') ?></td>
        <td><?= htmlspecialchars($row2['PERCENT_BY_VOLUME']) ?></td>
      </tr>

<?php
    }
}
?>

<?php
if ($selected_audit && $selected_audit_two){
	$audit_one_comp = oci_parse($conn, $query_str);
	oci_bind_by_name($audit_one_comp, ":audit_id",$selected_audit);
	oci_execute($audit_one_comp);
	$audit_two_comp = oci_parse($conn, $query_str_two);
	oci_bind_by_name($audit_two_comp, ":audit_id_two",$selected_audit_two);
	oci_execute($audit_two_comp);

	$audit_one_data=[];
	while ($r=oci_fetch_assoc($audit_one_comp)){
		$audit_one_data[$r['CATEGORY_NAME']] = [
		    'W' => $r['CATEGORY_WEIGHT'],
		    'PW' => $r['PERCENT_BY_WEIGHT'],
	            'V' => $r['PERCENT_BY_VOLUME']
		];
	}

        $audit_two_data=[];
        while ($r2=oci_fetch_assoc($audit_two_comp)){
                $audit_two_data[$r2['CATEGORY_NAME']] = [
		    'W' => $r2['CATEGORY_WEIGHT'],
		    'PW' => $r2['PERCENT_BY_WEIGHT'],
                    'V' => $r2['PERCENT_BY_VOLUME']
                ];
        }
        $comparison= array_intersect(array_keys($audit_one_data), array_keys($audit_two_data));
        
	echo "<tr><th colspan='7' style='background:#eaeaea;'>Comparison (Audit $selected_audit_two − Audit $selected_audit)</th></tr>";

      foreach ($comparison as $comp) {
	$dw = round($audit_two_data[$comp]['W'] - $audit_one_data[$comp]['W'], 2);
        $dpw = round($audit_two_data[$comp]['PW'] - $audit_one_data[$comp]['PW'], 2);
        $dv = round($audit_two_data[$comp]['V'] - $audit_one_data[$comp]['V'], 2);
	$cw = ($dw >= 0) ? 'pos' : 'neg';
	$cpw = ($dpw >=0) ? 'pos' : 'neg';
        $cv = ($dv >= 0) ? 'pos' : 'neg';
        echo "<tr style='background:#f8f8f8;'>
                <td colspan='3'>$comp Difference</td>
                <td>$comp</td>
		<td class='$cw'>$dw lbs</td>
                <td class='$cpw'>$dpw %</td>
                <td class='$cv'>$dv %</td>
              </tr>";
      }
      oci_free_statement($audit_one_comp);
      oci_free_statement($audit_two_comp);
    }




?>



</table>
<?php endif; ?>


<?php
    oci_free_statement($audit_list_stmt);
    if ($query_stmt) oci_free_statement($query_stmt);
    if ($query_stmt_two) oci_free_statement($query_stmt_two);
    oci_close($conn);
?>

<footer>
    <hr/>
    <p><a href="form.php">Back to Waste Audit Form</a> </p>
    
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


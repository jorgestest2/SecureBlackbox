<?php $sendBuffer = TRUE; ob_start(); ?>
<html>
<head>
<title>SecureBlackbox 2022 Demos - CAdES Signer</title>
<link rel="stylesheet" type="text/css" href="stylesheet.css">
<meta name="description" content="SecureBlackbox 2022 Demos - CAdES Signer">
</head>

<body>

<div id="content">
<h1>SecureBlackbox - Demo Pages</h1>
<h2>CAdES Signer</h2>
<p>A simple CAdES generator created with the CAdESSigner component. The sample supports creation of CAdES signatures of different conformance levels.</p>
<a href="default.php">[Other Demos]</a>
<hr/>

<?php
require_once('../include/secureblackbox_cadessigner.php');
require_once('../include/secureblackbox_certificatemanager.php');
require_once('../include/secureblackbox_const.php');

?>

<style>
table { width: 100% !important; }
td { white-space: nowrap; }
td input { width: 100%; }
td:last-child { width: 100%; }
</style>

<div width="90%">
  <form method=POST>
    <h2>CAdES Signing Demo</h2>
    
    <h3>General Options</h3>
    <table>
      <tr><td>Input File:</td><td><input type=text name=inputFile value=""></td></tr>
      <tr><td>Output File:</td><td><input type=text name=outputFile value=""></td></tr>
    </table>
    <br/>
    <br/>

    <b>Signing Options</b><br/>
    <table>
      <tr>
        <td>Signature Level:</td>
        <td>
          <select name="sigLevel">
            <option value="CADESVERIFIER_LEVEL_BES">BES</option>
            <option value="CADESVERIFIER_LEVEL_EPES">EPES</option>
            <option value="CADESVERIFIER_LEVEL_T">T</option>
            <option value="CADESVERIFIER_LEVEL_C">C</option>
            <option value="CADESVERIFIER_LEVEL_XTYPE_1">XType1</option>
            <option value="CADESVERIFIER_LEVEL_XTYPE_2">XType2</option>
            <option value="CADESVERIFIER_LEVEL_XLTYPE_1">XLType1</option>
            <option value="CADESVERIFIER_LEVEL_XLTYPE_2">XLType2</option>
            <option value="CADESVERIFIER_LEVEL_BASELINE_B">BaselineB</option>
            <option value="CADESVERIFIER_LEVEL_BASELINE_T">BaselineT</option>
            <option value="CADESVERIFIER_LEVEL_BASELINE_LT">BaselineLT</option>
            <option value="CADESVERIFIER_LEVEL_BASELINE_LTA">BaselineLTA</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_BES">ExtendedBES</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_EPES">ExtendedEPES</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_T">ExtendedT</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_C">ExtendedC</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_XTYPE_1">ExtendedXType1</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_XTYPE_2">ExtendedXType2</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_XLTYPE_1">ExtendedXLType1</option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_XLTYPE_2">ExtendedXLType2 </option>
            <option value="CADESVERIFIER_LEVEL_EXTENDED_A">ExtendedA</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>Hash Algorithm:</td>
        <td>
          <select name="hashAlg">
            <option value=""></option>
            <option value="SHA1">SHA1</option>
            <option value="MD5">MD5</option>
            <option value="SHA256">SHA256</option>
            <option value="SHA384">SHA384</option>
            <option value="SHA512">SHA512</option>
            <option value="RIPEMD160">RIPEMD160</option>
          </select>
        </td>
      </tr>
    </table>
    <label> <input type="checkbox" name="detached" value="1" size="25"/> Detached </label>
    <br/>
    <br/>

    <b>Signing Certificate</b>
    <table>
      <tr><td>Certificate File:</td><td><input type=text name=sCertFile value=""></td></tr>
      <tr><td>Password:</td><td><input type=password name=sCertPass value=""></td></tr>
    </table>
    <br/>
    <br/>
    
    <b>Timestamp</b><br/><br/>
    <label> <input type="checkbox" name="useTimestamp" value="1" size="25"/> Request a timestamp from TSA server </label>
    <table>
      <tr><td>Timestamp Server:</td><td><input type=text name=timestampServer value=""></td></tr>
    </table>
    <input type="submit" value="Sign" />
  </form>
</div><br/>

<?php

function translateSignatureLevel($sigLevel){
  switch($sigLevel){
    case "CADESVERIFIER_LEVEL_BES":  return CADESVERIFIER_LEVEL_BES; break;
    case "CADESVERIFIER_LEVEL_EPES":  return CADESVERIFIER_LEVEL_EPES; break;
    case "CADESVERIFIER_LEVEL_T":  return CADESVERIFIER_LEVEL_T; break;
    case "CADESVERIFIER_LEVEL_C":  return CADESVERIFIER_LEVEL_C; break;
    case "CADESVERIFIER_LEVEL_XTYPE_1":  return CADESVERIFIER_LEVEL_XTYPE_1; break;
    case "CADESVERIFIER_LEVEL_XTYPE_2":  return CADESVERIFIER_LEVEL_XTYPE_2; break;
    case "CADESVERIFIER_LEVEL_XLTYPE_1":  return CADESVERIFIER_LEVEL_XLTYPE_1; break;
    case "CADESVERIFIER_LEVEL_XLTYPE_2":  return CADESVERIFIER_LEVEL_XLTYPE_2; break;
    case "CADESVERIFIER_LEVEL_BASELINE_B":  return CADESVERIFIER_LEVEL_BASELINE_B; break;
    case "CADESVERIFIER_LEVEL_BASELINE_T":  return CADESVERIFIER_LEVEL_BASELINE_T; break;
    case "CADESVERIFIER_LEVEL_BASELINE_LT":  return CADESVERIFIER_LEVEL_BASELINE_LT; break;
    case "CADESVERIFIER_LEVEL_BASELINE_LTA":  return CADESVERIFIER_LEVEL_BASELINE_LTA; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_BES":  return CADESVERIFIER_LEVEL_EXTENDED_BES; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_EPES":  return CADESVERIFIER_LEVEL_EXTENDED_EPES; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_T":  return CADESVERIFIER_LEVEL_EXTENDED_T; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_C":  return CADESVERIFIER_LEVEL_EXTENDED_C; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_XTYPE_1":  return CADESVERIFIER_LEVEL_EXTENDED_XTYPE_1; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_XTYPE_2":  return CADESVERIFIER_LEVEL_EXTENDED_XTYPE_2; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_XLTYPE_1":  return CADESVERIFIER_LEVEL_EXTENDED_XLTYPE_1; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_XLTYPE_2":  return CADESVERIFIER_LEVEL_EXTENDED_XLTYPE_2; break;
    case "CADESVERIFIER_LEVEL_EXTENDED_A":  return CADESVERIFIER_LEVEL_EXTENDED_A; break;
    default: return CADESVERIFIER_LEVEL_UNKNOWN; break;
  }
}

  if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $cadessigner = new SecureBlackbox_CAdESSigner();
    $certmgr = new SecureBlackBox_CertificateManager();
    
    try {
      // General options
      $cadessigner->setInputFile($_REQUEST['inputFile']);
      $cadessigner->setOutputFile($_REQUEST['outputFile']);
      
      // Signing options
      $certmgr->doImportFromFile($_REQUEST['sCertFile'], $_REQUEST['sCertPass']);
      $cadessigner->setSigningCertHandle($certmgr->getCertHandle());
      
      $sigLevel = translateSignatureLevel($_REQUEST['sigLevel']);
      $hashAlg = $_REQUEST['hashAlg'];
      if (!empty($hashAlg)) {$cadessigner->setHashAlgorithm($hashAlg);}
      $detached = (isset($_REQUEST['detached']) && (($_REQUEST['detached'] == 'yes') || ($_REQUEST['detached'] == '1')));

      if (isset($_REQUEST['useTimestamp']) && (($_REQUEST['useTimestamp'] == 'yes') || ($_REQUEST['useTimestamp'] == '1')))
      {
        $cadessigner->setTimestampServer($_REQUEST['timestampServer']);
      }

      $cadessigner->doSign($sigLevel, $detached);
      echo "<h2>Signing Successful</h2>";
    }
    catch (exception $e) {
      echo "<h2>Signing Failure (Details Below)</h2><p>" . $e->getMessage() . "</p>";
    }
  }
?>
<br/>
<br/>
<br/>
<hr/>
NOTE: These pages are simple demos, and by no means complete applications.  They
are intended to illustrate the usage of the SecureBlackbox objects in a simple,
straightforward way.  What we are hoping to demonstrate is how simple it is to
program with our components.  If you want to know more about them, or if you have
questions, please visit <a href="http://www.nsoftware.com/?demopg-SBPHA" target="_blank">www.nsoftware.com</a> or
contact our technical <a href="http://www.nsoftware.com/support/">support</a>.
<br/>
<br/>
Copyright (c) 2023 /n software inc. - All rights reserved.
<br/>
<br/>
</div>

<div id="footer">
<center>
SecureBlackbox 2022 - Copyright (c) 2023 /n software inc. - All rights reserved. - For more information, please visit our website at <a href="http://www.nsoftware.com/?demopg-SBPHA" target="_blank">www.nsoftware.com</a>.
</center>
</div>

</body>
</html>

<?php if ($sendBuffer) ob_end_flush(); else ob_end_clean(); ?>

Documentation
=================================

This documentation provides explanations for additional parameters added in OSGEM to create a functioning model only. For explanation of the other parameters, please see the ReadTheDocs links referred to in the README.

OSeMOSYS
*******************************
These parameters are found in the input file for the OSeMOSYS-PuLP portion of OSGEM.

+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| Parameter                              | Description                                                                                                                                                                       | Unit           |
+========================================+===================================================================================================================================================================================+================+
| LCOEResidInv[r,t,y]                    | Annualized investment cost of assets existing at the start of the model period before discounting.                                                                                | Monetary units |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| LCOETagFuel[r,f,y]                     | Binary parameter tagging the fuels that contribute to energy that makes us the denominator in the LCOE formula. It has value 1 for the technologies contributing, 0 otherwise.    | Dimensionless  |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
| LCOETagTechnology[r,t,y]               | Binary parameter tagging the technologies that contribute to costs that go into the numerator of the LCOE formula. It has value 1 for the technologies contributing, 0 otherwise. | Dimensionless  |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+

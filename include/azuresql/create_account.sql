-- =============================================================================================================================
-- Create SQL Login template for Azure SQL Database, Azure Synapse Analytics Database, and Azure Synapse SQL Analytics on-demand
-- =============================================================================================================================

CREATE LOGIN [thanhphat] 
	WITH PASSWORD = 'Th!nhphat2609' 
GO

-- =============================================================================================================================
-- Create Microsoft Entra Login template for Azure SQL Database, Azure Synapse Analytics Database, and Azure Synapse SQL Analytics on-demand
-- =============================================================================================================================

-- CREATE LOGIN <Microsoft Entra Principal, sysname, login_name> FROM EXTERNAL PROVIDER
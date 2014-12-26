galaxy
======

Configuration files and scripts to integrate [ODoSE](http://www.odose.nl/) with [Galaxy](http://getgalaxy.org).

See also: https://github.com/ODoSE/odose.nl

Install Galaxy as per their instructions.

- Add a new folder `odosenl` in `galaxy-dist/tools/`. 
- Copy/symlink `*.py` & `*.xml` from both https://github.com/ODoSE/odose.nl and https://github.com/ODoSE/odose.nl to `galaxy-dist/tools/odosenl` 
- Add in `galaxy-dist/config/tool_conf.xml`:
```xml
        <section name="Ortholog Direction of Selection Engine" id="odosenl">
            <tool file="odosenl/load_prokaryotes.xml" />
            <tool file="odosenl/upload_genomes.xml" />
            <tool file="odosenl/select_taxa.xml" />
            <tool file="odosenl/translate.xml" />
            <tool file="odosenl/run_orthomcl.xml" />
            <tool file="odosenl/extract_orthologs.xml" />
            <tool file="odosenl/align_trim_orthologs.xml" />
            <tool file="odosenl/concatemer_tree.xml" />
            <tool file="odosenl/filter_orthologs.xml" />
            <tool file="odosenl/crosstable_gene_ids.xml" />
            <tool file="odosenl/compare_taxa.xml" />
            <tool file="odosenl/split_by_taxa.xml" />
            <tool file="odosenl/run_codeml.xml" />
            <tool file="odosenl/run_phipack.xml" />
            <tool file="odosenl/calculations.xml" />
            <tool file="odosenl/versions.xml" />
        </section>
    ```
- Add in `galaxy-dist/config/datatypes_conf.xml`:
```xml
        <datatype extension="pid.tsv" type="galaxy.datatypes.tabular:Tabular" display_in_upload="true"/>
        <datatype extension="groups.tsv" type="galaxy.datatypes.tabular:Tabular" display_in_upload="true"/>
        <datatype extension="gbk.zip" type="galaxy.datatypes.binary:Binary" mimetype="application/zip" display_in_upload="true"/>
        <datatype extension="ffn.zip" type="galaxy.datatypes.binary:Binary" mimetype="application/zip" display_in_upload="true"/>     
        <datatype extension="faa.zip" type="galaxy.datatypes.binary:Binary" mimetype="application/zip" display_in_upload="true"/>
        <datatype extension="ort.zip" type="galaxy.datatypes.binary:Binary" mimetype="application/zip" display_in_upload="true"/>
        <datatype extension="sico.zip" type="galaxy.datatypes.binary:Binary" mimetype="application/zip" display_in_upload="true"/>
    ```

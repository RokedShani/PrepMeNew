import { Button, Grid, Text, Spacer } from "@nextui-org/react";
import Link from "next/link";

 const Segel : any = () =>{
const segels = ['SG','SD','SH','SV'];
    return(
      <div><>
           <Spacer y={5} />
             <Text
               h1
               size={60}
               css={{
                 textGradient: "45deg, $purple600 -20%, $pink600 100%",
               }}
               weight="bold"
             >
               ספר לנו, באיזה סגל אתה?
             </Text>

             {segels.map((segel) => { 
                return (
                createButton(segel)              
             )})}
       </> 
       </div>);
      }

 const createButton = (segelName: string) => {
  return <Grid.Container gap={2} justify="center">
   <Grid xs={3}>
     <Link href="subject">
     <Button size="xl" shadow color="gradient" rounded ghost>
       {segelName}
     </Button>
     </Link>
   </Grid>
 </Grid.Container>
}

 export default Segel;
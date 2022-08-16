import { Link, Button, Grid, Text, Spacer } from "@nextui-org/react";

const Subject : any = () =>{
const subjects = ['עת"פ','JAVA&OOP','DB','DEVOPS','WEB'];
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
                איזה מקצוע אתה רוצה לראות
             </Text>

             {subjects.map((subject) => { 
                return (
                createButton(subject)              
             )})}
       </> 
       </div>);
      }

 const createButton = (subjectName: string) => {
  return <Grid.Container gap={2} justify="center">
   <Grid xs={3}>
     <Link href="table">
     <Button size="xl" shadow color="gradient" rounded ghost>
       {subjectName}
     </Button>
     </Link>
   </Grid> 
 </Grid.Container>
}

 export default Subject;